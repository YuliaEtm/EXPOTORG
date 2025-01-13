import requests
import os
import dotenv
import DB_SQL2
import allure
import pytest

dotenv.load_dotenv()
BASE_URL = os.getenv('BASE_URL_DEV2')


def post_greate_mat(body):
    # создание нового материала
    response = requests.post(f"{BASE_URL}/api/materials/", json=body)
    return response


def get_by_ext_num(ext_num):
    # проверка, что материал создан через Swagger по ext_num
    response = requests.get(f"{BASE_URL}/api/materials/by_ext_num/?ext_num={ext_num}")
    return response


payload = {
    "ext_id": "datatest-7ad2-4b42-b304-e1444b941d82",
    "ext_num": "06011",
    "name": "без кромки",
    "depth": 1,
    "length": 1,
    "width": 1,
    "cover": "",
    "structure": "",
    "texture": "LONG_SIDE",
    "edge_material_ext_ids": []
    }


@pytest.mark.smoke
@allure.description('Создаем новый материал без кромки, проверяем запись в БД, удаляем')
def test_post_greate_mat():
    with allure.step("создание нового"):
        response = post_greate_mat(payload)
    with allure.step("проверка создания"):
        assert response.status_code == 200, 'материал не создан'

    with allure.step(" GET проверка создания по ext_num"):
        response1 = get_by_ext_num(payload["ext_num"])
        assert response1.status_code == 200, 'материал не найден'

    #with allure.step("Удаление через подключение к БД и проверка выполнения"):
        #DB_SQL2.db_deleted_param('materials', 'ext_num', payload["ext_num"])

        #response2 = get_by_ext_num(payload["ext_num"])
        #assert response2.status_code == 400, 'материал не удален'


payload_edge2 = {
    "ext_id": "datatest-7ad2-4b42-b304-e1444b941d88",
    "ext_num": "06012",
    "name": "с 2 кромками",
    "depth": 1,
    "length": 1,
    "width": 1,
    "cover": "",
    "structure": "",
    "texture": "LONG_SIDE",
    "edge_material_ext_ids": ["9c439966-4f36-11ea-90af-0050569c2c21", "d4771887-30d5-11e7-80f0-005056be21bb"]
    }


@pytest.mark.regression
@allure.description('Создаем новый материал с 2-мя кромками, проверяем запись в БД, удаляем')
def test_post_greate_mat_edge():

    with allure.step("создание нового"):
        response = post_greate_mat(payload_edge2)
    with allure.step("проверка создания"):

        assert response.status_code == 200, 'материал не создан'
        # assert response.json()['result'] is True

    with allure.step(" GET проверка создания по ext_num"):
        response1 = get_by_ext_num(payload_edge2["ext_num"])
        assert response1.status_code == 200, 'материал не найден'
        # нужна проверка записи в таблицу material_item_edge ручной тест?

    with allure.step("Удаление через подключение к БД и проверка выполнения"):
        DB_SQL2.db_deleted_param('materials', 'ext_num', payload_edge2["ext_num"])

        response2 = get_by_ext_num(payload_edge2["ext_num"])
        assert response2.status_code == 400, 'материал не удален'


payload_not_existed_edge = {
    "ext_id": "datatest-7ad2-4b42-b304-e1444b911111",
    "ext_num": "06012",
    "name": "кромка не существ",
    "depth": 1,
    "length": 1,
    "width": 1,
    "cover": "",
    "structure": "",
    "texture": "LONG_SIDE",
    "edge_material_ext_ids": ["not existed edge"]
    }


@pytest.mark.regression
@allure.description('Создаем новый материал с кромкой отсутствующей в базе, проверяем запись в БД')
def test_post_greate_mat_not_existed_edge():

    with allure.step("создание нового"):
        response = requests.post(f"{BASE_URL}/api/materials/", json=payload_not_existed_edge)

    with allure.step("проверка создания в описании нет КОДА"):
        assert response.status_code == 404, 'материал возможно создан'
        assert response.json()['result'] is False

    with allure.step(" GET проверка создания по ext_num в описании нет КОДА"):
        response1 = get_by_ext_num(payload_not_existed_edge["ext_num"])
        assert response1.status_code == 400, 'материал возможно создан'


payload_not_existed_texture = {
    "ext_id": "datatest-7ad2-4b42-b304-e1444b911111",
    "ext_num": "09015",
    "name": "без текстуры",
    "depth": 1,
    "length": 1,
    "width": 1,
    "cover": "",
    "structure": "",
    "texture": "",
    "edge_material_ext_ids": []
}


@pytest.mark.exteded_failed
@allure.description('Создаем новый материал без заполненного поля "texture", проверяем отсутствие БД')
def test_post_greate_mat_not_existed_texture():

    with allure.step("создание нового"):
        response = requests.post(f"{BASE_URL}/api/materials/", json=payload_not_existed_texture)

    with allure.step("проверка ошибки создания"):
        assert response.status_code == 420, 'материал возможно создан без текстуры'

    with allure.step(" GET проверка ошибки создания по ext_num в описании нет КОДА400"):
        response1 = get_by_ext_num(payload_not_existed_edge["ext_num"])
        assert response1.status_code == 400, 'материал возможно создан'


texture = ['LONG_SIDE', 'SHORT_SIDE', 'WITHOUT_TEXTURE']


@pytest.mark.exteded
@allure.description("Создаем новый материал с полем  texture из ['LONG_SIDE', 'SHORT_SIDE', 'WITHOUT_TEXTURE']")
@pytest.mark.parametrize('num', texture)
def test_post_greate_mat_texture(num):

    payload_texture = {
        "ext_id": "datatest-7ad2-4b42-b304-e1444b941d82",
        "ext_num": "06011",
        "name": "без кромки",
        "depth": 1,
        "length": 1,
        "width": 1,
        "cover": "",
        "structure": "",
        "texture": num,
        "edge_material_ext_ids": []
    }
    with allure.step("создание нового"):
        response = post_greate_mat(payload_texture)

    with allure.step("проверка создания"):
        assert response.status_code == 200, 'материал не создан'
    # assert response.json()['result'] is True

    with allure.step(" GET проверка создания по ext_num"):
        response1 = get_by_ext_num(payload_texture["ext_num"])
        assert response1.status_code == 200, 'материал не найден'

    with allure.step("Удаление через подключение к БД и проверка выполнения"):
        DB_SQL2.db_deleted_param('materials', 'ext_num', payload_texture["ext_num"])

        response2 = get_by_ext_num(payload_texture["ext_num"])
        assert response2.status_code == 400, 'материал не удален'
