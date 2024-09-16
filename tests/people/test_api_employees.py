import requests
from tests.test_constants import successful_status_code

ENDPOINT = 'http://127.0.0.1:8000/api/'
COUNT = 5  # Общее количество работников


def test_get_list_employees():
    response = requests.get(ENDPOINT + 'employees/')

    assert response.status_code == successful_status_code

    data = response.json()

    assert data['count'] == COUNT

    assert len(data['data']) == COUNT

    for i in range(COUNT):
        assert data['data'][i]['id'] == i + 1


def test_get_paginaton_limit_employees():
    response = requests.get(ENDPOINT + f'employees/?limit=1')

    assert response.status_code == successful_status_code

    data = response.json()

    assert data['count'] == COUNT

    assert len(data['data']) == 1


def test_get_paginaton_offset_employees():
    response = requests.get(ENDPOINT + f'employees/?offset=1')

    assert response.status_code == successful_status_code

    data = response.json()

    assert data['count'] == COUNT

    assert data['data'][0]['id'] == 2


def test_get_paginaton_limof_employees():
    response = requests.get(ENDPOINT + f'employees/?limit=1&offset=1')

    assert response.status_code == successful_status_code

    data = response.json()

    assert data['count'] == COUNT

    assert len(data['data']) == 1

    assert data['data'][0]['id'] == 2


def test_get_filter_employees():
    response = requests.get(ENDPOINT + f'employees/?name=Политыко%20Софья')

    assert response.status_code == successful_status_code

    data = response.json()

    assert data['count'] == COUNT

    assert len(data['data']) == 1


def test_get_ordering_employees():
    response = requests.get(ENDPOINT + f'employees/?ordering=age')

    assert response.status_code == successful_status_code

    data = response.json()

    assert data['count'] == COUNT

    assert data['data'] == sorted(data['data'], key=lambda d: d['age'])
