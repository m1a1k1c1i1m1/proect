import os
from dotenv import load_dotenv
from random import choice
from string import ascii_uppercase
from dataclasses import dataclass

load_dotenv('../.env')


name = ''.join(choice(ascii_uppercase) for i in range(5)).lower()

email = f'{name}@mailforspam.com'
url = f'https://www.mailforspam.com/mail/{name}/1'

post_body = {
    "email": email,
    "name": "Сергей",
    "password": 'Faren12345',
    "userEula": {
        "accepted": "true"
    }
}


body_sing_up = {
    "login": email,
    "password": 'Faren12345'
}


# json для передачи при отправления запроса нна страницу av
body = {
    "page": 1,
    "properties": [
        {
            "name": "price_currency",
            "value": 2
        }
    ],
    "sorting": 4
}


# header
HEDERS = {
            "Content-type": "application/json",
            "X-Api-Key": None,
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36"
                          " (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
            "Origin": "https://cars.av.by",
            "Referer": "https://cars.av.by/",
            "Sec-Ch-Ua": 'Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
            "Sec-Ch-Ua-Mobile": "?1",
            "Sec-Ch-Ua-Platform": "Android",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-dir_av",
}


# todo для главной страницы
main_todo_cars = {
    'req': 'post',
    'page_all_flag': False,
    'type_page': 'cars',
    'body': body,
    'Url': os.getenv('URL_CARS'),
    'name': str(body['page'])
}

main_todo_phone = {
    'req': 'get',
    'page_all_flag': False,
    'type_page': 'cars',
    'body': body,
    'Url': os.getenv('URL_CARS'),
    'name': str(body['page'])
}


@dataclass
class User:
    user: dict
    data_time: object


@dataclass
class Data:
    url: str
    body: dict
    headers: dict


def format_json(data):
    try:
        new_value = dict()
        usd = data['price']['usd']['amount']
        byn = data['price']['byn']['amount']
        new_car = data['properties']
        for items in new_car:
            key_name = items['name']
            value = items['value']
            if value != True:
                new_value.update({f'{key_name}': value})
        new_value.update({
            'locationName': data['locationName'],
            'sellerName': data['sellerName'],
            'refreshedAt': data['refreshedAt'],
            'publishedAt': data['publishedAt'],
            'publicUrl': data['publicUrl'],
            'price_byn': byn,
            'price_usd': usd,
            'name_todo': str(data['id'])
        })
        return new_value
    except Exception as error:
        print(error)

