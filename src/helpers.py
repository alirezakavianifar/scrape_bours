import os
import selenium
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import re
import pandas as pd
from datetime import datetime
from contextlib import contextmanager
from tqdm import tqdm
from dateutil.parser import parse
from functools import wraps
from collections import defaultdict
from bs4 import BeautifulSoup
import requests

from src.constants import SCRAPER_CONFIG

def go_to_url_two(url='http://www.varzesh3.ir'):
    try:
        # Set a timeout of 20 seconds
        response = requests.get(url=url, timeout=20)
    except requests.exceptions.Timeout:
        print("The request timed out")
        raise
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        raise
    return response

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{folder_path}' created.")
    else:
        print(f"Folder '{folder_path}' already exists.")


def url_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        print(f"\nscraping {kwargs['url']}")
        result = func(*args, **kwargs)  # Execute the function
        end_time = time.time()  # Record the end time
        execution_time = end_time - start_time  # Calculate the execution time
        # print(f"It took {execution_time:.4f} seconds")
        return result
    return wrapper

# Extended regex pattern to match different date formats, including dates with no spaces around them
date_pattern = (
    r'\b(?:\d{1,2}[./-]\d{1,2}[./-]\d{2,4}|'     # Matches formats like 01/01/2020 or 01-01-2020
    r'\d{4}[./-]\d{1,2}[./-]\d{1,2}|'             # Matches formats like 2020/01/01 or 2020-01-01
    r'\d{1,2}\s*\w+\s*\d{2,4}|'                   # Matches formats like 1 January 2020 or 1January2020
    r'\w+\s*\d{1,2},?\s*\d{2,4}|'                 # Matches formats like January 1, 2020 or January1,2020
    r'\d{1,2}\s*\w+,\s*\d{4}|'                    # Matches formats like 1 January, 2020 or 1January,2020
    r'\w+\s*\d{1,2}\s*\d{4})\b'                   # Matches formats like June 4 2024 or June4 2024
)

# Function to extract dates from text using dateutil.parser
def extract_dates(text, num_dates=None):
    try:
        matches = re.findall(date_pattern, text)
        parsed_dates = set()
        for match in matches:
            try:
                # Parse the date using dateutil.parser with fuzzy=True to handle various formats
                parsed_date = parse(match, dayfirst=True, fuzzy=True)
                parsed_dates.add(parsed_date.strftime('%Y-%m-%d'))
            except ValueError:
                continue
        sorted_dates = sorted(parsed_dates)
        if num_dates:
            sorted_dates = sorted_dates[:num_dates]
        return ', '.join(sorted_dates) if sorted_dates else None
    except:
        return text

@contextmanager
def init_driver(pathsave, driver_type='chrome', headless=False, prefs={'maximize': False, 'zoom': '1.0'},
                driver=None, info={}, use_proxy=False, disable_popups=False, port=0, *args, **kwargs):
    """
    Context manager for initializing and managing a Selenium WebDriver.

    Args:
    - pathsave (str): The directory path where downloaded files will be saved.
    - driver_type (str): Type of the WebDriver, default is 'chrome'.
    - headless (bool): Whether to run the browser in headless mode, default is False.
    - prefs (dict): Dictionary of preferences for the WebDriver.
    - driver: Existing WebDriver instance, if provided.
    - info (dict): Additional information, if needed.
    - port (int): The port to use for ChromeDriver.
    - *args, **kwargs: Additional arguments and keyword arguments.

    Yields:
    - driver: The initialized WebDriver instance.
    """
    if driver_type == 'chrome':
        # Configuring options for Chrome WebDriver
        options = ChromeOptions()
        if headless:
            options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        if port:
            options.add_argument(f'--remote-debugging-port={port}')
        prefs = {'download.default_directory': pathsave}
        options.add_argument("start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option("prefs", {"download.default_directory": pathsave})

        # Initialize Chrome WebDriver
        service = ChromeService()
        driver = webdriver.Chrome(service=service, options=options)
        driver.set_page_load_timeout(15)  # Set the page load timeout to 15 seconds

        # Switching to the first window handle
        driver.switch_to.window(driver.window_handles[0])

    try:
        yield driver  # Providing the initialized WebDriver to the user
    finally:
        driver.quit()  # Ensuring WebDriver is properly closed after use
        
def extract_data(driver, info, elms_info):
    
    table_data = []
    html_source = driver.page_source
    soup = BeautifulSoup(html_source, 'lxml')
    # Text to find within the HTML
    text_to_find = 'نتیجه ای برای نمایش وجود ندارد.'
    # Find all <td> tags with specific text
    results = [td_tag.get_text(strip=True) for td_tag in soup.find_all('td')]
    
    if text_to_find in results:
        return driver, info, table_data        
    
    elements = soup.find_all(elms_info['tag_name'], class_=elms_info['class_'])
    for elm in elements:
        try:
            # Extract data from each <td> in the rows
            row_data = []
            notice_link = ""
            for cell in elm.find_all('td'):
                # Get text inside the cell, stripping extra whitespace
                cell_text = cell.get_text(strip=True)
                row_data.append(cell_text)
                if cell.attrs['data-th'] == 'اطلاعیه':
                    notice_link = cell.find('a')['href'] if cell.find('a') else ''
                    parsed_url = urlparse(info['url'])
                    # Extract the base URL
                    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}{notice_link}"
                    row_data.append(base_url)
                
            table_data.append(row_data)
        except:
            continue
    return driver, info, table_data

def generic_scrape(driver, info, elements_info, pagination_info=None, url=None):
    data = defaultdict(list)

    if pagination_info:
        try:
            if pagination_info['pages_xpaths']:
                for item in pagination_info['pages_xpaths']:
                    time.sleep(2)
                    driver.find_element(By.XPATH, item).click()
                
            num_pages = int(WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.XPATH, pagination_info['pages_xpath']))
            ).text)
        except:
            num_pages = 500
        for i in range(2, num_pages + 1):
            try:
                html_source = driver.page_source
                soup = BeautifulSoup(html_source, 'lxml')
                elements = soup.find_all(elements_info['element_tag'], class_=elements_info['element_class'])
                if len(elements) == 0:
                    try:
                        response = go_to_url_two(url=url)
                        soup = BeautifulSoup(response.text, 'html5lib')
                    except:
                        ...
                page_not_found, table_data = extract_data(soup, elements_info, url)
                if page_not_found or i > pagination_info['limit_pages']:
                    break
                next_page_url = pagination_info['url_template'].format(page_number=i)
                driver.get(next_page_url)
            except Exception as e:
                ...
    else:
        page_number = 1
        while True:
            try:
                html_source = driver.page_source
                soup = BeautifulSoup(html_source, 'lxml')
                elements = soup.find_all(elements_info['element_tag'], class_=elements_info['element_class'])
                if len(elements) == 0:
                    try:
                        response = go_to_url_two(url=url)
                        soup = BeautifulSoup(response.text, 'html5lib')
                    except:
                        ...
                page_not_found, table_data = extract_data(soup, elements_info, url)
                if page_not_found:
                    break
                page_number += 1
                next_page_url = pagination_info['url_template'].format(page_number=page_number)
                driver.get(next_page_url)
            except:
                break
    
    if not data:
        print('data not captured...')
        data['title'].append('No title found')
        data['date'].append('No date found')
        data['link'].append('No link found')
    
    df = pd.DataFrame(data)
    df = df[df['title'] != '']
    # df = df[df['link'] != '']
    # df = df[df['date'] != '']
    df.drop_duplicates(inplace=True)
    if not df.empty:
        df.insert(0, 'Url', driver.current_url)
        sanitized_url = re.sub(r'[^\w\s-]', '', driver.current_url)
        df.to_excel(f'output_files/{sanitized_url}.xlsx', index=False)

    return driver, info

# Generalized scrape function
def scrape_news(driver, info, config_key):
    config = SCRAPER_CONFIG[config_key]
    elements_info = config['elements_info']
    pagination_info = config.get('pagination_info')
    
    return generic_scrape(driver, info, elements_info, pagination_info, config_key)


def list_files(directory, extension):
    return [it.path for it in os.scandir(directory) if it.is_file() and it.name.endswith('.' + extension)]

# Example usage:
# Specify the directory path where you want to unzip files
# unzip_files('/path/to/directory', remove=True)

def extract_website_name(text):

    # Improved regex pattern:
    website_pattern = r"(https?://)?(www\.)?([^\s/?]+)\.([^\s/?]+)"  # Capture entire domain name

    match = re.search(website_pattern, text)

    if match:
        website_name = match.group(3)  # Extract the third capturing group for domain name
        return website_name
    else:
        print("No website name found")

def combine_excel_files(excel_files, output_filename):
  
    with pd.ExcelWriter(output_filename) as writer:
        ind = 1

        for filename, df in excel_files.items():
            try:
                filename = extract_website_name(filename)
                filename = filename.split('\\')[-1]
                filename = str(ind)
                    
                df.to_excel(writer, sheet_name=filename, index=False)
                ind += 1
            except FileNotFoundError:
                print(f"Error: File not found - {filename}")

def combine_results(directory=r'output_files'):
    excel_fils = list_files(directory=directory, extension='xlsx')
    excel_files = {}
    for excel_file in excel_fils:
        final_df = pd.read_excel(excel_file)
        # Apply the function to the DataFrame column
        final_df.fillna({'date': final_df['title']}, inplace=True)
        final_df['extracted_date'] = final_df['date'].apply(lambda x: extract_dates(x, num_dates=1))
        # final_df['extracted_date'] = final_df['extracted_date'].apply(lambda x: extract_dates(x, num_dates=1))
        final_df.drop(columns=['date'], inplace=True)
        # final_df.dropna(subset=['extracted_date'], inplace=True)
        final_df.rename(columns={'extracted_date': 'date'}, inplace=True)
        col_orders = ['Url', 'title', 'date', 'link']
        final_df = final_df[col_orders]
        excel_files[excel_file] = final_df

    combine_excel_files(excel_files, 'final_results.xlsx')

def combine_results_(directory=r'output_files'):
    excel_fils = list_files(directory=directory, extension='xlsx')
    lst = []
    for excel_file in excel_fils:
        df = pd.read_excel(excel_file)
        lst.append(df)

    final_df = pd.concat(lst)

    # Apply the function to the DataFrame column
    final_df['extracted_date'] = final_df['date'].apply(lambda x: extract_dates(x, num_dates=1))
    final_df.fillna({'extracted_date': df['title']}, inplace=True)
    final_df['extracted_date'] = final_df['extracted_date'].apply(lambda x: extract_dates(x, num_dates=1))
    final_df.drop(columns=['date'], inplace=True)
    final_df.dropna(subset=['extracted_date'], inplace=True)
    final_df.rename(columns={'extracted_date': 'date'}, inplace=True)
    col_orders = ['Url', 'title', 'date', 'link']
    final_df = final_df[col_orders]
    final_df.to_excel(r'final_output/final_results.xlsx')

def scrape_news_with_params(driver, info, source):
    return scrape_news(driver, info, source)

def get_nemads(driver, info):
    WebDriverWait(driver, 4).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div/div/nav/div/a[2]'))
            ).click()
    
    select_elm = WebDriverWait(driver, 4).until(
                EC.presence_of_element_located((By.NAME, 'per_page'))
            )
    # Create a Select object
    select = Select(select_elm)

    # Select the last option by index
    select.select_by_index(len(select.options) - 1)
    
    # Locate the <ul> element with class "pagination bootpag"
    ul_element = driver.find_element(By.CLASS_NAME, 'pagination.bootpag')

    # Find all <li> elements within the <ul>
    li_elements = ul_element.find_elements(By.TAG_NAME, 'li')

    # Get the text of the last <li> element
    last_li_text = li_elements[-1].text
    
    # Extract only the number using regular expressions
    last_li_number = int(re.findall(r'\d+', last_li_text)[0])
    
    info['num_pages'] = last_li_number
    
    # Locate the <thead> element
    thead_element = driver.find_element(By.TAG_NAME, 'thead')

    # Find all <th> elements within the <thead>
    th_elements = thead_element.find_elements(By.TAG_NAME, 'th')

    # Extract the text from each <th> element and store it in a list
    header_values = [th.text for th in th_elements]
    
    info['header_values'] = header_values
    
    return driver, info

def scrape_nemad_info(driver, info, output_path=None):
    table_datas = []
    info['url'] = info['url'].replace('#scroll_to_results', '&page=')
    for page_number in range(2, info['num_pages'] + 2):
        try:
            
            driver, info, table_data = extract_data(driver, info, elms_info={'tag_name': 'tr', 'class_':'gradeX'})
            if table_data:
                table_datas.extend(table_data)
                driver.get(f"{info['url']}{page_number}")
            else:
                break
            
        except:
            ...
    if table_datas:
        df = pd.DataFrame(table_datas, columns=info['header_values']).to_excel(os.path.join(output_path, f"{info['nemad']}.xlsx"))
    
    try:
        driver.get('https://my.codal.ir/')
    except:
        ...
    
    return driver, info

def search_nemad(driver, info, nemad):
    last_li_number = 1
    
    WebDriverWait(driver, 4).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'select2-search__field'))
            ).send_keys(nemad)
    
    time.sleep(1)
    # Simulate pressing the "Enter" key
    WebDriverWait(driver, 4).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'select2-search__field'))
            ).send_keys(Keys.ENTER)
    
    select_elm = WebDriverWait(driver, 4).until(
                EC.presence_of_element_located((By.NAME, 'per_page'))
            )
    # Create a Select object
    select = Select(select_elm)

    # Select the last option by index
    select.select_by_index(len(select.options) - 1)
    
    # Locate the <ul> element with class "pagination bootpag"
    try:
        ul_element = driver.find_element(By.CLASS_NAME, 'pagination.bootpag')

        # Find all <li> elements within the <ul>
        li_elements = ul_element.find_elements(By.TAG_NAME, 'li')

        # Get the text of the last <li> element
        last_li_text = li_elements[-1].text
        
        # Extract only the number using regular expressions
        last_li_number = int(re.findall(r'\d+', last_li_text)[0])
        
    except:
        pass
    
    info['num_pages'] = last_li_number
    # Locate the <thead> element
    thead_element = driver.find_element(By.TAG_NAME, 'thead')

    # Find all <th> elements within the <thead>
    th_elements = thead_element.find_elements(By.TAG_NAME, 'th')

    # Extract the text from each <th> element and store it in a list
    header_values = [th.text for th in th_elements]
    header_values.insert(4, 'لینک اطلاعیه')
    
    info['header_values'] = header_values
    
    info['url'] = driver.current_url
    info['symbol'] = re.search(r'symbol=(\d+)', driver.current_url).group(1) # Using regular expression to find the symbol number
    
    info['nemad'] = nemad
    
    return driver, info
            
    
            

