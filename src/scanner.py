import requests
import json
import time
import os
import zipfile
from src.model.articleDetail import Article
from src.digitecScrapy import DigitecScrapy
from dotenv import load_dotenv

from src.model.custom_exception import HitRateLimitException, NotFoundException
from src.utils.logger import logger, LogLevel
from src.statusPrinter import Status, StatusPrinter

load_dotenv()

DISPLAY_NAME = str(os.getenv("DISPLAY_NAME"))
TOKEN = str(os.getenv("TOKEN"))
SERVER_URL = str(os.getenv("SERVER_URL"))

ZIP_PATH = "./data.zip"
DATA_PATH = "./data"

class Scanner():
    def __init__(self, output_length: int = 10) -> None:
        if not os.path.exists(DATA_PATH): os.mkdir(DATA_PATH)

        self.last_article: list[Article] = []
        self.printer = StatusPrinter(30,18,65)
        self.output_length = output_length
        self.run_scan: bool = True
        self.error_counter = 0
        logger(LogLevel.INFO, f"{DISPLAY_NAME} started client")

    def start(self) -> None:
        self.__clean_up()
        
        while True:
            try:
                print("Start Batch-Scan")
                batch = self.__get_batch()
                print(batch)
                self.__scan(batch['number_list'], batch['interval'], batch['id'])
                self.__zip_and_delete_data()
                self.__send_data(batch['id'])
                self.last_article = []
                print("End Batch-Scan")
                self.error_counter = 0
                time.sleep(2)
            except Exception as e:
                self.error_counter += 1
                print(f'{self.error_counter}. Error: {e}')
                if self.error_counter == 1:
                    time.sleep(5)
                elif self.error_counter > 1 and self.error_counter < 30:
                    time.sleep(60)
                elif self.error_counter >= 30:
                    time.sleep(600)
                    try:
                        logger(LogLevel.ERROR, f"{DISPLAY_NAME} failed to start scan")
                    except:
                        pass

    def stop(self) -> None:
        self.run_scan = False

    def __get_batch(self):
        url = f"{SERVER_URL}/job/get_batch/"
        ip_address = self.__get_ip_address()
        data = {"token": TOKEN, 
                "ip": ip_address,
                "display_name": DISPLAY_NAME}
        return requests.post(url, data=json.dumps(data)).json()
    
    def __get_ip_address(self) -> str:
        try:
            response = requests.get('https://httpbin.org/ip')
            if response.status_code == 200:
                return response.json()['origin']
            else:
                print("Failed to retrieve public IP")
                return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    
    def __scan(self, numbers: list[int], interval: float, id: str) -> None:
        digitecScrapy = DigitecScrapy()

        for article_number in numbers:
            start_time = time.time()

            attempt_counter = 0

            while True:
                has_error = False
                try:
                    article = digitecScrapy.get_article_details(article_number, False, True, False, DATA_PATH)
                    self.last_article.append(article)
                except NotFoundException as e:
                    pass
                except HitRateLimitException as e:
                    has_error = True
                    time.sleep(interval)
                except Exception as e:
                    logger(LogLevel.ERROR, f"{DISPLAY_NAME} failed to scan {article_number} (undefined error)")
                    print(f"Not specified error: {e}")

                attempt_counter += 1
                
                if not has_error:
                    break
                if has_error and attempt_counter > 10:
                    logger(LogLevel.ERROR, f"Fail to scan: {article_number}")
                    break

            status = Status(id, numbers[0], numbers[-1], article_number ,len(self.last_article), self.last_article)
            print("")
            self.printer.print_status(status, self.output_length)

            duration = (time.time() - start_time)
            if duration < interval:
                time.sleep((interval-duration))

    def __zip_and_delete_data(self) -> None:
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

    def __send_data(self, id) -> None:
        url = f"{SERVER_URL}/job/upload_batch/"
        data = {"id": id}
        files = {'file': open(ZIP_PATH, 'rb')}
        response = requests.post(url, files=files, data=data)
        if response.status_code == 200:
            print(f'{response.status_code}: {response.text}')
        elif response.status_code == 404:
            logger(LogLevel.ERROR, f"{DISPLAY_NAME} failed to upload data: 404 Error")
        else:
            print(f"{response.status_code}: Error during upload")
        if os.path.exists(ZIP_PATH):
            os.remove(ZIP_PATH)

    def __clean_up(self) -> None:
        for file in os.listdir(DATA_PATH):
            full_path = os.path.join(DATA_PATH, file)
            if os.path.isfile(full_path):
                os.remove(full_path)

        if os.path.exists(ZIP_PATH):
            os.remove(ZIP_PATH)