import requests
from packages.util import *
import os


def post_requests(data) -> str:
    req = requests.post(url=data.url, json=data.body, headers=data.headers).text
    if cheсk_folder(os.getenv('PAGE_DIR')):
        log_info(f'[crawler.py]: папкаа уже создана')
    else:
        create_folder(os.getenv('PAGE_DIR'))
        log_info(f'[crawler.py]: create folder {os.getenv("PAGE_DIR")}')
    seve_file(req, 'cars', os.getenv('PAGE_DIR'))
    return req


def get_requests(data) -> str:
    req = requests.post(url=data.url, headers=data.headers).text
    if cheсk_folder(os.getenv('PAGE_DIR')):
        log_info(f'[crawler.py]: папкаа уже создана')
    else:
        create_folder(os.getenv('PAGE_DIR'))
        log_info(f'[crawler.py]: create folder {os.getenv("PAGE_DIR")}')
    seve_file(req, 'phone', os.getenv('PAGE_DIR'))
    return req
