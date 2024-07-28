import pandas as pd  # Importing the pandas library for data manipulation and analysis
from helpers import url_logger, init_driver, combine_results, \
    scrape_news_with_params, SCRAPER_CONFIG, create_folder_if_not_exists, get_nemads, scrape_nemad_info, search_nemad
from tqdm import tqdm  # Importing tqdm for progress bar visualization

# Setting the scrape flag to True to enable the scraping process
scrape = True
collect_nemads = False
base_url = 'https://my.codal.ir/fa/'

if scrape:
    create_folder_if_not_exists('output_files')

# Reading the Excel file into a DataFrame
df = pd.read_excel(r'final.xlsx')

# Decorating the function with wrap_it_with_params to handle parameters for the scraping process
@url_logger
def go_to_url(driver, info, url='http://www.varzesh3.ir'):
    try:
        driver.get(url)
    except:
        ...# Navigating to the specified URL using the provided web driver

    return driver, info  # Returning the driver and additional info

# Executing the scraping process if the scrape flag is set to True
if scrape:
    with init_driver(pathsave=None, driver_type='chrome', headless=False) as driver:
        # Iterating over the first 60 rows of the DataFrame
        driver, info = go_to_url(driver=driver, info={}, url=base_url)  # Navigating to the URL
        
        if collect_nemads:
            driver, info = get_nemads(driver, info)
            driver, info = scrape_nemad_info(driver=driver, info=info)
        else:
            for index, row in tqdm(df.iloc[1355:,:].iterrows()):
                try:
                    driver, info = search_nemad(driver, info, row['نماد'])
                    driver, info = scrape_nemad_info(driver=driver, info=info)
                
                except:
                    driver.get('https://my.codal.ir/')
                    continue
                
                  # Checking if there is a specific scraping function for the URL
                # driver, info = scraping_functions[url](driver=driver, info=info)  # Calling the specific scraping function

# Combining the results from the scraping process
combine_results()
