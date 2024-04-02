from articleDetail import Article
from digitecScrapy import DigitecScrapy
import time

def scan(start_number: int, min_time: int):
    digitecScrapy = DigitecScrapy()

    for i in range(22557840):
        start_time = time.time()
        try:
            article_data = digitecScrapy.get_article_details(start_number + i, print_out=False, safe_zio=True, safe_json=False)
            print(f'{article_data.product_type:<40} {article_data.number} - {article_data.name:<40}')
        except Exception as e:
            print(f'Error - {start_number + i}  {e}')
        
        duration = (time.time() - start_time)*1000
        
        if duration < min_time:
            time.sleep((min_time-duration)/1000)

#scan(22557847)
scan(22557847-10, 100)