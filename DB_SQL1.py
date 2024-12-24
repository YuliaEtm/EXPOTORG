import psycopg2 as ps
from psycopg2 import OperationalError
import os
import dotenv

dotenv.load_dotenv()
host = os.getenv('HOST_POSTGRES_DEV2')
user = os.getenv('USER_POSTGRES_DEV2')
password = os.getenv('PASSWORD_POSTGRES_DEV2')
database = os.getenv('DATABASE_POSTGRES_DEV2')


def create_connection(db_name, db_user, db_password, db_host):
    connection = None
    try:
        connection = ps.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
        )
        print("C PostgreSQL соединение установлено")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


 # Создаем соединение
connection = create_connection(database,user,password,host)

cursor = connection.cursor()  # Создаем программный объект, обязательно

table_name = 'materials'
material_ext_num = "18124"


def get_ext_num(table, ext_num):
    # GET ищем в таблице  по ext_num
    request_to_read_data = f'SELECT*FROM {table} WHERE ext_num=%s'
    cursor.execute(request_to_read_data, (ext_num,))
    data = cursor.fetchall()
    for row in data:
        print(data)


get_ext_num(table_name, material_ext_num)

# def delete_ext_num(table, ext_num):
#     # Удаляем из таблицы по ext_num)
#     request_to_delete_data = f'DELETE FROM {table} WHERE ext_num=%s'
#     cursor.execute(request_to_delete_data, (ext_num,))
#     connection.commit()
#
#
# delete_ext_num(table_name, material_ext_num)
#
#
cursor.close()  # выход обязательно
connection.close()  # выход обязательно
