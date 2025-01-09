import pytest
import psycopg2 as ps
from psycopg2 import OperationalError
import os
import dotenv
from psycopg2.extras import DictCursor
from psycopg2.extras import NamedTupleCursor
import psycopg2

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
        print("Соединение установлено")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


def db_get_id(table_name, column_name, search_param):
    # Извлекаем id элемента из таблицы table_name по значению search_param из колонки column_name
    with create_connection(database, user, password, host) as connection:
        with connection.cursor() as cursor:
            try:
                request_to_read_data = f'SELECT id  FROM {table_name} WHERE {column_name}=%s'
                cursor.execute(request_to_read_data, (search_param,))
                data = cursor.fetchone()
                data_id = data[0]
                return data_id
            except Exception:
                print(f'значение {search_param} в колонке {column_name} в таблице {table_name} не найдено')


def db_deleted_param(table_name, column_name, delete_param):
    # Удаляем элемент по delete_param из колонки column_name из таблицы table_name
    with create_connection(database, user, password, host) as connection:
        with connection.cursor() as cursor:

            request_to_delete_data = f'DELETE FROM {table_name} WHERE {column_name}=%s'
            cursor.execute(request_to_delete_data, (delete_param,))
            connection.commit()
