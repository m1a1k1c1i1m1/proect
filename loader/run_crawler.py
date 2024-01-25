import json
import os
import sys
from time import sleep
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)


from packages.util import *
from packages.json_content import *
from loader import crawler
from datetime import datetime, timedelta


def main():
    try:
        items = os.listdir(os.getenv('FOLDER_AV'))
        for item in items:
            match item:
                case 'log_av.json':
                    time_stemp = open_file(item, os.getenv('FOLDER_AV'))["data_time"]
                    data_create_user = datetime.fromtimestamp(time_stemp)
                    if datetime.now() - data_create_user > timedelta(days=1):
                        print(1)
                    else:
                        list_folder = os.listdir(os.getenv('TODO_DIR'))
                        if len(list_folder) == 0:
                            sleep(5)
                        else:
                            for file in list_folder:
                                data = open_file(file, os.getenv('TODO_DIR'))
                            match data["type_page"]:
                                case 'cars':
                                    X_Api_Key = open_file(item, os.getenv('FOLDER_AV'))["user"]["apiKey"]
                                    HEDERS.update({"X-Api-Key": X_Api_Key})
                                case 'phone':
                                    X_Api_Key = os.getenv('API_KEY')
                                    HEDERS.update({"X-Api-Key": X_Api_Key})
                            data_info_req = Data(url=data["Url"], body=data['body'], headers=HEDERS)
                            match data['req']:
                                case 'post':
                                    crawler.post_requests(data_info_req)
                                case _:
                                    crawler.get_requests(data_info_req)
                            delet_file(os.getenv('TODO_DIR') + file, os.getenv('TODO_DIR'))
    except Exception as ex:
        print(f'ошибка: {ex} возникает в файле run_crawler.py в функции main')


if __name__ == "__main__":
    while True:
        main()
