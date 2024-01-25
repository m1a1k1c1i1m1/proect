import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from packages.util import *
import requests
import re
import json
import time
from packages.json_content import *
from datetime import datetime



def sing_up():
    loop_flag = True
    req_sing_up = Data(headers=HEDERS, url=os.getenv('URL_SING_UP'), body=post_body)
    req = requests.post(url=req_sing_up.url, json=req_sing_up.body, headers=req_sing_up.headers)
    if req.status_code == 204:
        log_info('запрос отправили для перехода после регистрации')
        while loop_flag:
            req_email = requests.get(url).content.decode()
            log.info('скачали страницу с сообщением')
            url_av = re.search(r"https://av\.by/confirm-registration\?token=\w+", req_email)
            if url_av != None:
                req_get = Data(url=url_av.group(0), headers=HEDERS, body=body)
                requests_sing_up = requests.get(url=req_get.url, headers=req_get.headers)
                if requests_sing_up.status_code == 200:
                    req_sing_in = Data(url=os.getenv('URL_SING_IN'), body=body_sing_up, headers=HEDERS)
                    sing_in = requests.post(url=req_sing_in.url, json=req_sing_in.body, headers=req_sing_in.headers).content.decode('utf-8')
                    loop_flag = False
                    data_user = {
                        'user': json.loads(sing_in),
                        'data_time': datetime.timestamp(datetime.now())
                    }
                    log.info('пользователь зарегистрирован')
                    return data_user
            else:
                log.info('нет еще сообщения')
                time.sleep(2)
