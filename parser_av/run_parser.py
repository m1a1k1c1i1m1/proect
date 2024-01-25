import json
import os
import sys
from time import sleep
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from parser_av.parser import Parser

from packages import util
from packages.json_content import *
scrapy = Parser()


def main():
    list_folder_page = os.listdir(os.getenv('PAGE_DIR'))
    if len(list_folder_page) == 0:
        sleep(3)
    else:
        for item in list_folder_page:
            data = util.open_file(item, os.getenv('PAGE_DIR'))
        new_data = json.loads(data)['adverts']
        scrapy.pars(new_data)
        util.delet_file(os.getenv('PAGE_DIR') + item, os.getenv('PAGE_DIR'))


if __name__ == '__main__':
    while True:
        try:
            main()
            sleep(60)
        except Exception as ex:
            print(ex)
