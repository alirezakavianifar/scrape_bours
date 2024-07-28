import numpy as np
import pandas as pd
import os
from concurrent.futures import ThreadPoolExecutor, wait, ProcessPoolExecutor
from helpers import url_logger, init_driver, combine_results, \
    scrape_news_with_params, SCRAPER_CONFIG, create_folder_if_not_exists, get_nemads, scrape_nemad_info, search_nemad
from tqdm import tqdm
import logging

# Setting up logging
logging.basicConfig(level=logging.INFO)

# Checkpoint file prefix
CHECKPOINT_PREFIX = 'checkpoint_'

def load_checkpoint(df_name):
    checkpoint_file = f"{CHECKPOINT_PREFIX}{df_name}.txt"
    if os.path.exists(checkpoint_file):
        with open(checkpoint_file, 'r') as file:
            return int(file.read().strip())
    return 0

def save_checkpoint(df_name, index):
    checkpoint_file = f"{CHECKPOINT_PREFIX}{df_name}.txt"
    with open(checkpoint_file, 'w') as file:
        file.write(str(index))

@url_logger
def go_to_url(driver, info, url='http://www.varzesh3.ir'):
    try:
        driver.get(url)
    except Exception as e:
        logging.error(f"Error navigating to URL {url}: {e}")
        raise e

    return driver, info

def scrape_data(df, base_url, collect_nemads, output_path=None, pathsave=None, driver_type='chrome', headless=False, port=0):
    df_name = df.index.name or 'df'
    start_index = load_checkpoint(df_name)
    logging.info(f"Starting scrape from index {start_index}")

    with init_driver(pathsave=pathsave, driver_type=driver_type, headless=headless, port=port) as driver:
        driver, info = go_to_url(driver=driver, info={}, url=base_url)
        
        if collect_nemads:
            driver, info = get_nemads(driver, info)
            driver, info = scrape_nemad_info(driver=driver, info=info)
        else:
            for index, row in tqdm(df.iloc[start_index:].iterrows(), initial=start_index, total=len(df)):
                try:
                    driver, info = search_nemad(driver, info, row['نماد'])
                    driver, info = scrape_nemad_info(driver=driver, info=info, output_path=output_path)
                    save_checkpoint(df_name, index)
                except Exception as e:
                    logging.error(f"Error processing row {index}: {e}")
                    driver.get('https://my.codal.ir/')
                    continue

def schedule_scraping(dfs, base_url, collect_nemads, output_path=None, pathsave=None, driver_type='chrome', headless=False):
    with ProcessPoolExecutor(len(dfs)) as executor:
        jobs = [
            executor.submit(scrape_data, df, base_url, collect_nemads, output_path, pathsave, driver_type, headless, port)
            for port, df in zip(range(9222, 9222 + len(dfs)), dfs)
        ]
        wait(jobs)

if __name__ == '__main__':
    scrape = True
    collect_nemads = False
    base_url = 'https://my.codal.ir/fa/'
    output_path = 'output_files'

    if scrape:
        create_folder_if_not_exists(output_path)

    df = pd.read_excel(r'final.xlsx')
    lst_dfs = np.array_split(df, 3)

    schedule_scraping(lst_dfs, base_url, collect_nemads, output_path, headless=False)
    combine_results()
