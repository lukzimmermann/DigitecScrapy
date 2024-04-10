import requests
import json
import time
import os
import zipfile
from articleDetail import Article
from digitecScrapy import DigitecScrapy
from dotenv import load_dotenv

from statusPrinter import Status, StatusPrinter

load_dotenv()

DISPLAY_NAME = str(os.getenv("DISPLAY_NAME"))
TOKEN = str(os.getenv("TOKEN"))
SERVER_URL = str(os.getenv("SERVER_URL"))
IS_TOR_ACTIVE = os.getenv("IS_TOR_ACTIVE").lower() in ['true', 'yes', '1']

ZIP_PATH = "./data.zip"
DATA_PATH = "./data"

class Scanner():
    def __init__(self, output_length: int = 10) -> None:
        if not os.path.exists(DATA_PATH): os.mkdir(DATA_PATH)

        self.last_article: list[Article] = []
        self.printer = StatusPrinter(30,18,65)
        self.output_length = output_length
        self.run_scan: bool = True
        self.proxies = {
            'http': 'socks5h://localhost:9050',
            'https': 'socks5h://localhost:9050'
        }
        

    def start(self):
        self.__clean_up()
        
        while True:
            try:
                print("Start Batch-Scan")
                batch = self.__get_batch()
                print(batch)
                print(len(batch['number_list']))
                self.__scan(batch['number_list'], batch['interval'], batch['id'])
                self.__zip_and_delete_data()
                self.__send_data(batch['id'])
                self.last_article = []
                print("End Batch-Scan")
                time.sleep(2)
                break
            except Exception as e:
                print(f"Error: {e}")
                time.sleep(60)

    def stop(self):
        self.run_scan = False

    def __get_batch(self):
        url = f"{SERVER_URL}/jobs/get_batch/"
        ip_address = self.__get_ip_address()
        data = {"token": TOKEN, 
                "ip": ip_address,
                "display_name": DISPLAY_NAME}
        return requests.post(url, data=json.dumps(data)).json()
    
    def __get_ip_address(self) -> str:
        try:
            response = None
            if IS_TOR_ACTIVE:
                response = requests.get('https://httpbin.org/ip', proxies=self.proxies)
            else:
                response = requests.get('https://httpbin.org/ip')

            if response.status_code == 200:
                return response.json()['origin']
            else:
                print("Failed to retrieve public IP")
                return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    
    def __scan(self, numbers: list[int], interval: float, id: str):
        digitecScrapy = DigitecScrapy(self.proxies)

        for article_number in numbers:
            start_time = time.time()

            attempt_counter = 0

            while True:
                has_error = False
                try:
                    article = digitecScrapy.get_article_details(article_number, False, True, False, DATA_PATH)
                    self.last_article.append(article)
                except Exception as e:
                    print(str(e))
                    print(f'ERROR - {article_number} - counter={attempt_counter}')
                
                    has_error = True
                    time.sleep(1)

                attempt_counter += 1
                
                if not has_error:
                    break
                if has_error and attempt_counter > 10:
                    break
                    
            
            status = Status(id, numbers[0], numbers[-1], article_number,len(self.last_article), self.last_article)
            print("")
            self.printer.print_status(status, self.output_length)

            duration = (time.time() - start_time)
            if duration < interval:
                time.sleep((interval-duration))

    def __zip_and_delete_data(self):
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

    def __send_data(self, id):
        url = f"{SERVER_URL}/jobs/upload_batch/"
        data = {"id": id}
        files = {'file': open(ZIP_PATH, 'rb')}
        response = requests.post(url, files=files, data=data)
        print("Upload successful")
        if os.path.exists(ZIP_PATH):
            os.remove(ZIP_PATH)

    def __clean_up(self):
        for file in os.listdir(DATA_PATH):
            full_path = os.path.join(DATA_PATH, file)
            if os.path.isfile(full_path):
                os.remove(full_path)

        if os.path.exists(ZIP_PATH):
            os.remove(ZIP_PATH)