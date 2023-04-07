import pymysql

host = 'localhost'
user = 'mark'
password = 'password'
db_name = 'user'


def conect_db(data):
    try:
        conection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        print('conect db')

        try:
            with conection.cursor() as cursor:
                 creare_table_qwery = "CREATE TABLE `users_testing`(id int AUTO_INCREMENT," \
                                      "name varchar(32)," \
                                      "email varchar(50)," \
                                      "password varchar(35), PRIMARY KEY(id));"
                 try:
                    cursor.execute(creare_table_qwery)
                    print('create table')
                 except Exception as Ex:
                     print('Таблица уже создана')

            with conection.cursor() as cursor:
                insert_quwery = f"INSERT INTO `user`.`users_testing` (`name`, `email`, `password`) " \
                                f"VALUES ('{data[0]}','{data[1]}', '{data[2]}');"
                cursor.execute(insert_quwery)
                print(f'пользователь: {data[0]} сахранен')
                conection.commit()
        finally:
            conection.close()
    except Exception as Ex:
        print('conection fatal')
        print(Ex)
