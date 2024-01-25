import time
from packages.util import *
from packages.json_content import (
    format_json
)
from datetime import (
    datetime,
    timedelta
)


class Parser:

    def pars(self, data):
        for item in data:
            data_time = item['refreshedAt'].replace('T', ' ').split('+')[0]
            new = datetime.strptime(data_time, '%Y-%m-%d %H:%M:%S')
            if datetime.now() - new > timedelta(hours=3, minutes=13):
                log_info('нам машина не подходит')
            else:
                car_json = format_json(item)
                if not os.path.isdir(os.getenv('CAR_DIR')):
                    create_folder(os.getenv('CAR_DIR'))
                    seve_file(car_json, str(car_json['name_todo']), os.getenv('CAR_DIR'))
                    log_info('[parser.py] save car')
                else:
                    seve_file(car_json, str(car_json['name_todo']), os.getenv('CAR_DIR'))
                    log_info('[parser.py] save car')
