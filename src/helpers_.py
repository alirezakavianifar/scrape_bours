import os
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
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


def wrap_it_with_params(num_tries=3, time_out=20,
                        driver_based=False, detrimental=True,
                        clean_up=False, keep_alive=False, record_process_details=False):
    def wrap_it(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal num_tries
            result = None
            i = 0
            while (True):
                if i < num_tries:
                    # Update success information in kwargs
                    if 'info' in kwargs:
                        kwargs['info']['success'] = True
                    else:
                        kwargs['info'] = {}
                        kwargs['info']['success'] = True

                    # Log function call
                    print(
                        f'function {func.__name__} is called at {datetime.now()}')
                    try:
                        # Measure function execution time
                        start = time.process_time()
                        if record_process_details:
                            ...

                        result, info = func(*args, **kwargs)
                        end = time.process_time()
                        elapsed_time = end - start

                        # Check if elapsed time exceeds the timeout
                        if elapsed_time > time_out:
                            result = None

                        # Check for unsuccessful execution or termination conditions
                        if ((result is None) or ((not info['success']) and (not keep_alive))):
                            raise Exception
                        else:
                            # Log function completion
                            print(
                                f'function {func.__name__} is finished at {datetime.now()}')
                            break
                    except Exception as e:
                        # Handle exceptions and retry
                        print(
                            f'Exception occurred in function {func.__name__}, the error is {e}')
                        time.sleep(1)
                        i += 1
                        if i < num_tries:
                            print(
                                f'retrying function {func.__name__} for {i} times at {datetime.now()}')
                else:
                    try:
                        # Update info for unsuccessful execution
                        kwargs['info']['keep_alive'] = keep_alive
                        kwargs['info']['success'] = False

                        # Handle driver-based scenarios
                        if driver_based:
                            if 'driver' in kwargs:
                                driver = kwargs['driver']
                            else:
                                for item in args:
                                    if isinstance(item, selenium.webdriver.firefox.webdriver.WebDriver):
                                        driver = item
                            result = driver

                        # Perform clean-up actions
                        if clean_up:
                            ...

                        # Perform detrimental actions
                        if detrimental:
                            driver.quit()

                        # Terminate function if keep_alive is False
                        if not keep_alive:
                            # raise Exception
                            pass

                        return driver, kwargs['info']
                    except Exception as e:
                        # Handle exceptions during cleanup
                        raise Exception

            return result, info

            # The following code is unreachable due to the return statement above.
            # Keeping it commented out for clarity.
            # if isinstance(result, tuple):
            #     res, success = result
            #     if not success:
            #         return result
            # return result, True
        return wrapper
    return wrap_it

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
    
# Decorating the function with wrap_it_with_params to handle parameters for the scraping process
def go_to_url(url='http://www.varzesh3.ir'):
    try:
        response = requests.get(url=url)
    except Exception as e:
        print(e)
        raise Exception
    return response  # Returning the driver and additional info

@contextmanager
def init_driver(pathsave, driver_type='firefox', headless=False, prefs={'maximize': False,
                                                                        'zoom': '1.0'}, driver=None,
                info={}, use_proxy=False, disable_popups=False, *args, **kwargs):
    """
    Context manager for initializing and managing a Selenium WebDriver.

    Args:
    - pathsave (str): The directory path where downloaded files will be saved.
    - driver_type (str): Type of the WebDriver, default is 'firefox'.
    - headless (bool): Whether to run the browser in headless mode, default is False.
    - prefs (dict): Dictionary of preferences for the WebDriver.
    - driver: Existing WebDriver instance, if provided.
    - info (dict): Additional information, if needed.
    - *args, **kwargs: Additional arguments and keyword arguments.

    Yields:
    - driver: The initialized WebDriver instance.

    Usage:
    with init_driver(pathsave='/path/to/downloads') as driver:
        # Your code using the WebDriver goes here

    Note: Ensure proper installation of Selenium and WebDriver executables.

    """
    if driver_type == 'chrome':
        # Configuring options for Chrome WebDriver
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless")
        prefs = {'download.default_directory': pathsave}
        options.add_argument("start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option("prefs", {"download.default_directory": pathsave})

        # Initialize Chrome WebDriver
        service = ChromeService()
        driver = webdriver.Chrome(service=service, options=options)

        # Switching to the first window handle
        driver.window_handles
        driver.switch_to.window(driver.window_handles[0])

    try:
        yield driver  # Providing the initialized WebDriver to the user

    finally:
        driver.quit()  # Ensuring WebDriver is properly closed after use

def generic_scrape(url, response, elements_info, pagination_info=None):
    data = defaultdict(list)
    pages_num = 1

    def extract_data(soup, elements_info):
        page_not_found = False
        title = ''
        date = ''
        link = ''
        elements = soup.find_all(elements_info['element_tag'], class_=elements_info['element_class'])
        if len(elements) == 0:
            print('error')
        for elm in elements:
            try:
                title_element = elm.find(elements_info['title_tag'], class_=elements_info['title_class'])
                if title_element.get('title') is not None:
                    title = title_element.get('title')
                else:
                    title = title_element.get_text(strip=True) if title_element else ''

                error_element = elm.find(elements_info['error_tag'], class_=elements_info['error_class'])
                error_title = error_element.get_text(strip=True) if error_element else ''
                if error_title:
                    print('Page not found')
                    page_not_found = True
                    break
                if title == '':
                    print('Title not found')
                    
                date_element = elm.find(elements_info['date_tag'], class_=elements_info['date_class'])
                if date_element is not None:
                    if date_element.get('title') is not None:
                        date = date_element.get('title')
                    else:
                        date = date_element.get_text(strip=True) if date_element else ''

                if elm.name == 'a' and elm.get('href'):
                    if title == '' and elm.get('title'):
                        title = elm.get('title')
                    link = elm.get('href')
                else:
                    link_element = elm.find(elements_info['link_tag'], class_=elements_info['link_class'])
                    link = link_element['href'] if link_element else url

                data['title'].append(title)
                data['date'].append(date)
                data['link'].append(link)
            except:
                continue

        return page_not_found

    try:
        # soup = BeautifulSoup(response.text, 'html.parser')
        # soup = BeautifulSoup(response.text, 'lxml')
        soup = BeautifulSoup(response.text, 'html5lib')
        page_not_found = extract_data(soup, elements_info)

        if page_not_found:
            print('done')
        else:
            if pagination_info['limit_pages'] > 1:
                while pages_num < pagination_info['limit_pages']:
                    pages_num += 1
                    next_page_url = pagination_info['url_template'].format(page_number=pages_num)
                    response = go_to_url(next_page_url)
                    soup = BeautifulSoup(response.text, 'html5lib')
                    page_not_found = extract_data(soup, elements_info)

    except Exception as e:
        print(e)
    
    if not data:
        print('data not captured...')
    else:

        df = pd.DataFrame(data)
        df = df[df['title'] != '']
        # df = df[df['link'] != '']
        # df = df[df['date'] != '']
        df.drop_duplicates(inplace=True)
        if not df.empty:
            df.insert(0, 'Url', url)
            sanitized_url = re.sub(r'[^\w\s-]', '', url)
            df.to_excel(f'output_files\{sanitized_url}.xlsx', index=False)


# Generalized scrape function
def scrape_news(config_key, response):
    config = SCRAPER_CONFIG[config_key]
    elements_info = config['elements_info']
    pagination_info = config.get('pagination_info')
    
    return generic_scrape(url=config_key, response=response, elements_info=elements_info, pagination_info=pagination_info)


def list_files(directory, extension):
    return [it.path for it in os.scandir(directory) if it.is_file() and it.name.endswith('.' + extension)]

# Example usage:
# Specify the directory path where you want to unzip files
# unzip_files('/path/to/directory', remove=True)

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

def extract_website_name(text):

    # Improved regex pattern:
    website_pattern = r"(https?://)?(www\.)?([^\s/?]+)\.([^\s/?]+)"  # Capture entire domain name

    match = re.search(website_pattern, text)

    if match:
        website_name = match.group(3)  # Extract the third capturing group for domain name
        return website_name
    else:
        print("No website name found")

def combine_results(directory=r'output_files'):
    excel_fils = list_files(directory=directory, extension='xlsx')
    excel_files = {}
    for excel_file in excel_fils:
        final_df = pd.read_excel(excel_file)
        # Apply the function to the DataFrame column
        final_df['extracted_date'] = final_df['date'].apply(lambda x: extract_dates(x, num_dates=1))
        final_df.fillna({'extracted_date': final_df['title']}, inplace=True)
        final_df['extracted_date'] = final_df['extracted_date'].apply(lambda x: extract_dates(x, num_dates=1))
        final_df.drop(columns=['date'], inplace=True)
        final_df.dropna(subset=['extracted_date'], inplace=True)
        final_df.rename(columns={'extracted_date': 'date'}, inplace=True)
        col_orders = ['Url', 'title', 'date', 'link']
        final_df = final_df[col_orders]
        excel_files[excel_file] = final_df

    combine_excel_files(excel_files, 'final_results.xlsx')


def scrape_news_with_params(url, response):
    return scrape_news(url, response)
