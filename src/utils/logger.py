from enum import Enum
import os
import requests
from dotenv import load_dotenv

load_dotenv()

SERVER_URL = str(os.getenv("SERVER_URL"))
TOKEN = str(os.getenv("TOKEN"))

class LogLevel(str, Enum):
    CRITICAL = 'CRITICAL'
    ERROR = 'ERROR'
    WARNING = 'WARNING'
    INFO = 'INFO'
    DEBUG = 'DEBUG'
    NOTSET = 'NOTSET'

def logger(level: LogLevel, message: str):
    url = SERVER_URL + "/log/add/"
    data = {
        "token": TOKEN,
        "level": level.value,
        "module": "ScrapyClient",
        "message": message
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        print(f"{level.value} - {message}")
    else:
        print(f"Fail to send log: {level.value} - {message}")