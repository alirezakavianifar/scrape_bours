import pandas as pd  # Importing the pandas library for data manipulation and analysis
from src.helpers_ import combine_results, scrape_news_with_params, SCRAPER_CONFIG, go_to_url
from tqdm import tqdm  # Importing tqdm for progress bar visualization

# Setting the scrape flag to True to enable the scraping process
scrape = True

# Reading the Excel file into a DataFrame
df = pd.read_excel(r'src_files\Credit_Union_Entities.xlsx')


# Executing the scraping process if the scrape flag is set to True
if scrape:
    # Assuming the URLs are in columns named 'url1', 'url2', and 'url3'
    url_columns = ['Link_1', 'Link_2', 'Link_3']

    # Combine URLs from all columns into a single list, ignoring NaNs
    urls = df[url_columns].apply(lambda x: x.dropna().tolist(), axis=1).sum()
    # Iterating over the first 60 rows of the DataFrame
    for url in tqdm(urls[0:]):
        try:
            response = go_to_url(url=url) 
            if response.status_code == 200: # Navigating to the URL
                if url in SCRAPER_CONFIG:
                    scrape_news_with_params(url=url, response=response)
        except:
            continue
                
                  # Checking if there is a specific scraping function for the URL
                # driver, info = scraping_functions[url](driver=driver, info=info)  # Calling the specific scraping function

# Combining the results from the scraping process
combine_results()
