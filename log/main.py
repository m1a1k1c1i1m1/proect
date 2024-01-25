from log_sing_up import *
from time import sleep


while True:
    try:
        data = sing_up()
        seve_file(data, 'log_av', os.getenv('FOLDER_AV'))
        sleep(360)
    except ModuleNotFoundError as error:
        print(error)
