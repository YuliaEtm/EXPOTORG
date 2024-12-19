import requests
import allure
BASE_URL ="http://192.168.21.3:8000"
@allure.title(" POST Создание нового материалы без кромки")
@allure.testcase('https://team-0pkc.testit.software/projects/1/tests/3?isolatedSection=7cfd3124-54cb-490c-a03e-1a37ca875bd9','3')
def test_post_greate_mat():
# без кромки новый материал
    payload = {
    "ext_id": "940d86c7-7ad2-4b42-b304-e1444b941d82",
    "ext_num": "18124",
    "name": "18decemb",
    "depth": 1,
    "length": 1,
    "width": 1,
    "cover": "",
    "structure": "",
    "texture": "LONG_SIDE",
    "edge_material_ext_ids": []
    }
    response = requests.post(f"{BASE_URL}/api/materials/", json=payload)
    print(response)

    assert response.status_code == 200
    assert response.json()['result'] == True

def test_get_by_ext_num():
    response = requests.get(f"{BASE_URL}/api/materials/by_ext_num/?ext_num=18124")
    assert response.status_code == 200
    print(response)

def test_post_greate_mat_edge():
#с кромкой новый материал
    payload = {
    "ext_id": "940d86c7-7ad2-4b42-b304-e1444b941d88",
    "ext_num": "18125",
    "name": "18decembкромка",
    "depth": 1,
    "length": 1,
    "width": 1,
    "cover": "",
    "structure": "",
    "texture": "LONG_SIDE",
    "edge_material_ext_ids": ["9c439966-4f36-11ea-90af-0050569c2c21", "d4771887-30d5-11e7-80f0-005056be21bb"]
    }
    response = requests.post(f"{BASE_URL}/api/materials/", json=payload)
    print(response)

    assert response.status_code == 200
    assert response.json()['result'] == True
# нужна проверка записи в таблицу material_item_edge ручной тест

def test_post_greate_mat_not_existed_edge():
#с кромкой новый материал
    payload = {
    "ext_id": "940d86c7-7ad2-4b42-b304-e1444b941d88",
    "ext_num": "18126",
    "name": "18decemb кромка не существ",
    "depth": 1,
    "length": 1,
    "width": 1,
    "cover": "",
    "structure": "",
    "texture": "LONG_SIDE",
    "edge_material_ext_ids": ["not existed edge"]
    }
    response = requests.post(f"{BASE_URL}/api/materials/", json=payload)


    assert response.status_code == 404
    assert response.json()['result'] == False
    print(response.json())

def test_get_by_ext_num_not_existed():
    response = requests.get(f"{BASE_URL}/api/materials/by_ext_num/?ext_num=18126")
    assert response.status_code == 400


    #delete from materials
#where ext_num = '18124'



