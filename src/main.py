import pandas as pd  # Importing the pandas library for data manipulation and analysis
from src.helpers import url_logger, init_driver, combine_results, scrape_news_with_params, SCRAPER_CONFIG, create_folder_if_not_exists
from tqdm import tqdm  # Importing tqdm for progress bar visualization

# Setting the scrape flag to True to enable the scraping process
scrape = True

if scrape:
    create_folder_if_not_exists('output_files')

# Reading the Excel file into a DataFrame
df = pd.read_excel(r'Credit_Union_Entities.xlsx')

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
        # Assuming the URLs are in columns named 'url1', 'url2', and 'url3'
        url_columns = ['Link_1', 'Link_2', 'Link_3']

        # Combine URLs from all columns into a single list, ignoring NaNs
        urls = df[url_columns].apply(lambda x: x.dropna().tolist(), axis=1).sum()
        # Iterating over the first 60 rows of the DataFrame
        for url in tqdm(urls[8:10]):
            driver, info = go_to_url(driver=driver, info={}, url=url)  # Navigating to the URL
            if url in SCRAPER_CONFIG:
                driver, info = scrape_news_with_params(driver=driver, info=info, source=url)
                
                  # Checking if there is a specific scraping function for the URL
                # driver, info = scraping_functions[url](driver=driver, info=info)  # Calling the specific scraping function

# Combining the results from the scraping process
combine_results()
