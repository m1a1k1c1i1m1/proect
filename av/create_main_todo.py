import os
import sys
from time import sleep

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from packages.json_content import *
from packages.util import *

try:
    def create_main_todo() -> dict:
        if not os.path.isdir(os.getenv('TODO_DIR')):
            create_folder(os.getenv('TODO_DIR'))
            log_info(f'[create_main_todo.py]: create folder {os.getenv("TODO_DIR")}')
            create_todo(main_todo_cars, os.getenv('TODO_DIR'))
            log_info(f'[create_main_todo.py]: todo {main_todo_cars["Url"]} created in {os.getenv("TODO_DIR")}')
        else:
            create_todo(main_todo_cars, os.getenv('TODO_DIR'))
            log_info(f'[create_main_todo.py]: todo {main_todo_cars["Url"]} created in {os.getenv("TODO_DIR")}')
except Exception as ex:
    log_error(f'ошибка: {ex} возикла в файле main_todo')

if __name__ == "__main__":
    while True:
        create_main_todo()
        sleep(60)
