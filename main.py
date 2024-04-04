import requests
import json
import time
import os
import zipfile
from digitecScrapy import DigitecScrapy

SERVER_URL = 'https://www.dmining.ch'
DATA_PATH = '/Users/lukas/Documents/LocalProjects/digitecScrapy/data'
ZIP_PATH = '/Users/lukas/Documents/LocalProjects/digitecScrapy/data.zip'

def main():
    while True:
        try:
            batch = __get_batch()
            __scan(batch['start'], batch['end'], batch['interval'])
            __zip_and_delete_data()
            __send_data(batch['id'])
        except Exception as e:
            print(e)
            time.sleep(10)
        

def __get_batch():
    url = f"{SERVER_URL}/jobs/get_batch/"
    data = {"token":"3f284c4c087b0ee881642142009da4834a693c12c65a4bb5952d3fde3d5842be"}
    return requests.get(url, data=json.dumps(data)).json()

def __scan(start: int, end: int, interval: float):
    digitecScrapy = DigitecScrapy()
    for article_number in range(start, end+1):
        start_time = time.time()

        total = end -start
        current = article_number-start
        progres = float(current)/total*100

        try:
            article = digitecScrapy.get_article_details(article_number, False, True, False,DATA_PATH)
            print(f'{progres:.2f}% - {article.product_type:<40} {article.number} - {article.name:<40}')
        except Exception as e:
            print(f'{progres:.2f}% - {e} at {article_number}')

        duration = (time.time() - start_time)
        if duration < interval:
            time.sleep((interval-duration))

def __zip_and_delete_data():
    files_to_zip = []
    for file in os.listdir(DATA_PATH):
        full_path = os.path.join(DATA_PATH, file)
        if os.path.isfile(full_path):
            files_to_zip.append(full_path)
    
    zip_filename = "data.zip"
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for file in files_to_zip:
            zipf.write(file, os.path.basename(file))
            os.remove(file)

def __send_data(id):
    url = f"{SERVER_URL}/jobs/upload_batch/"
    data = {"id": id}
    files = {'file': open(ZIP_PATH, 'rb')}
    response = requests.post(url, files=files, data=data)
    print(response.json())
    if os.path.exists(ZIP_PATH):
        os.remove(ZIP_PATH)

if __name__ == "__main__":
    main()