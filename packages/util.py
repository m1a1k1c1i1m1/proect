import hashlib
import json
import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from loguru import logger as log
from datetime import datetime


def log_info(message):
    log.add("../av/debug.log", format=f"{datetime.now()}{message}", level="DEBUG")
    log.info(message)


def log_error(messeg):
    log.error(messeg)


def md_5(str_hash):
    hash = hashlib.md5()
    hash.update(str_hash.encode('utf-8'))
    name = hash.hexdigest()
    return name


def create_todo(todo, name_dir):
    with open(f'{name_dir}{md_5(todo["name"])}.json', 'w', encoding='utf-8') as File:
        json.dump(todo, File, indent=4)


def seve_file(data, name, name_dir):
    with open(f'{name_dir}{name}.json', 'w', encoding='utf-8') as File:
        json.dump(data, File, indent=4)


def open_todo(open_file, name_folder):
    with open(f'{name_folder}{open_file}', 'r', encoding='utf-8') as File:
        return File.read()


def open_file(open_file, name_folder):
    with open(f'{name_folder}{open_file}', 'r', encoding='utf-8') as File:
        data = File.read()
        return json.loads(data)


def cheсk_folder(name_dir):
    bool_info = os.path.exists(name_dir)
    match bool_info:
        case True:
            return True
        case _:
            return False


def create_folder(name_dir):
    os.mkdir(name_dir)


def delet_file(name_file, name_dir):
    os.remove(name_file)
    print(f'файл удален: {name_file} из папки {name_dir} ')













