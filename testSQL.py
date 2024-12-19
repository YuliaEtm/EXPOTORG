import psycopg2 as ps

# Создаем соединение
connection = ps.connect(
    host='192.168.21.3',
    user='industrial_stg',
    password='industrial_psw',
    database='industrial_stg'
)

cursor = connection.cursor()  # Создаем программный объект, обязательно

table_name = 'materials'
material_ext_num = "18124"


def get_ext_num(table,ext_num):
    request_to_read_data = f'SELECT*FROM {table} WHERE ext_num=%s'
    cursor.execute(request_to_read_data, (ext_num,))
    data = cursor.fetchall()
    for row in data:
        print(data)
#get_ext_num(table_name,material_ext_num)

def delete_ext_num(table,ext_num):
    request_to_delete_data = f'DELETE FROM {table} WHERE ext_num=%s'
    cursor.execute(request_to_delete_data, (ext_num,))
    connection.commit()
delete_ext_num(table_name,material_ext_num)

cursor.close()  # выход обязательно
connection.close()  # выход обязательно
