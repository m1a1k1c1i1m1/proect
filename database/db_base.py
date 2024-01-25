import pymysql.cursors


class Base:

    def check(self, name, name_table):

        connection = pymysql.connect(host='localhost', user='mark', password='password', database='cars', charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                name = name.replace('\'', '\\\'')
                sql = f"SELECT * FROM `{name_table}` WHERE name = '{name}';"
                result = cursor.execute(sql)
                return result
        except Exception:
            print(f'{Exception} {name} 1')
        finally:
            connection.close()

    def check_car(self, name, name_table):

        connection = pymysql.connect(host='localhost', user='mark', password='password', database='cars', charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                name = name.replace('\'', '\\\'')
                sql = f"SELECT * FROM `{name_table}` WHERE url_car = '{name}';"
                result = cursor.execute(sql)
                return result
        except Exception:
            print(f'{Exception}{name} 2')
        finally:
            connection.close()

    def get_id(self, name, name_db):
        connection = pymysql.connect(host='localhost', user='mark', password='password', database='cars', charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                name = name.replace('\'', '\\\'')
                sql = f"SELECT id FROM `{name_db}` WHERE name = '{name}';"
                cursor.execute(sql)
                result = cursor.fetchone()
                return result['id']
        except Exception as error:
            print(f'{error} {name} 3')
        finally:
            connection.close()

    def insert_info_marka(self, name):
        connection = pymysql.connect(host='localhost', user='mark', password='password', database='cars',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                name = name.replace('\'', '\\\'')
                # Create a new record
                sql = f"INSERT INTO `marka` (`name`) VALUES ('{name}');"
                cursor.execute(sql)

                # connection is not autocommit by default. So you must commit to save
                # your changes.
                connection.commit()
        except Exception:
            print(f'{Exception}{name} 4')
        finally:
            connection.close()

    def insert_info_model(self, name, id_marka):
        connection = pymysql.connect(host='localhost', user='mark', password='password', database='cars',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                # Create a new record
                name = name.replace('\'', '\\\'')
                sql = f"INSERT INTO `model` (`name`, `marka`) VALUES ('{name}', '{id_marka}');"
                cursor.execute(sql)

                # connection is not autocommit by default. So you must commit to save
                # your changes.
                connection.commit()
        except Exception:
            print(f'{Exception}{name} 5')
        finally:
            connection.close()

    def insert_info_car(self, data):
        connection = pymysql.connect(host='localhost', user='mark', password='password', database='cars',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                # Create a new record
                sql = (f"INSERT INTO `car` (`marka`, `model`, `year`, `url_car`, "
                       f"`locationName`, `publishedAt`, `refreshedAt`, "
                       f"`price_usd`, `price_by`, `engine_type`, `engine_capacity`,"
                       f"`transmission_type`, `drive_type`, `calor`, `sellerName`) VALUES ('"
                       f"{self.get_id(data['brand'], 'marka')}',"
                       f" '{self.get_id(data['model'], 'model')}', '{int(data['year'])}', '{data['publicUrl']}',"
                       f" '{data['locationName']}', '{data['publishedAt']}', '{data['refreshedAt']}',"
                       f"'{int(data['price_usd'])}', '{int(data['price_byn'])}', '{data['engine_type']}', "
                       f"'{float(data['engine_capacity'])}', '{data['transmission_type']}', "
                       f"'{data['drive_type']}', '{data['color']}', '{data['sellerName']}');")
                cursor.execute(sql)

                # connection is not autocommit by default. So you must commit to save
                # your changes.
                connection.commit()
        except Exception as error:
            print(f'{error} {data} 6')
        finally:
            connection.close()

    def get_all_car(self):
        connection = pymysql.connect(host='localhost', user='mark', password='password', database='cars', charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                sql = f"SELECT * FROM `car`;"
                cursor.execute(sql)
                result = cursor.fetchall()
                return result
        except Exception as error:
            print(f'{error} 7')
        finally:
            connection.close()

    def update_phone(self, data):
        connection = pymysql.connect(host='localhost', user='mark', password='password', database='cars',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                # Create a new record
                sql = f"update car set phone = '+{data['number']}' WHERE url_car = '{data['content']['name_todo']}';"
                cursor.execute(sql)

                # connection is not autocommit by default. So you must commit to save
                # your changes.
                connection.commit()
        except Exception as error:
            eror = f'{error} 8'
        finally:
            connection.close()

    def get_id_car(self, name, name_db):
        connection = pymysql.connect(host='localhost', user='mark', password='password', database='cars', charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                name = name.replace('\'', '\\\'')
                sql = f"SELECT id FROM `{name_db}` WHERE url_car = '{name}';"
                cursor.execute(sql)
                result = cursor.fetchone()
                return result['id']
        except Exception as error:
            print(f'{error} {name} 3')
        finally:
            connection.close()