import psycopg2 as ps
import os
import dotenv

dotenv.load_dotenv()
host = os.getenv('HOST_POSTGRES_DEV2')
user = os.getenv('USER_POSTGRES_DEV2')
password = os.getenv('PASSWORD_POSTGRES_DEV2')
database = os.getenv('DATABASE_POSTGRES_DEV2')
# Создаем соединение
connection = ps.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

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


get_ext_num(table_name,material_ext_num)


def delete_ext_num(table, ext_num):
    # Удаляем из таблицы по ext_num)
    request_to_delete_data = f'DELETE FROM {table} WHERE ext_num=%s'
    cursor.execute(request_to_delete_data, (ext_num,))
    connection.commit()


delete_ext_num(table_name, material_ext_num)
cursor.close()  # выход обязательно
connection.close()  # выход обязательно
