# Define the configuration dictionary
SCRAPER_CONFIG = {
    'https://my.codal.ir/fa/': {
        'elements_info': {
            'element_tag': 'tr', 'element_class': 'gradeX',
        },
        'pagination_info': {
            'url_template': 'https://my.codal.ir/fa/publishers/?company_type=&publisher_type=&industry=&status=&caution=&per_page=100&page={page_number}',
            'limit_pages': 50
        }
    },
}