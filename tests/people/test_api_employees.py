import requests

ENDPOINT = 'http://127.0.0.1:8000/api/'


def test_get_list_employees():
    response = requests.get(ENDPOINT + 'employees/')

    assert response.status_code == 200

    data = response.json()

    assert data['count'] == 5

    assert len(data['data']) == 5

    for i in range(1, 6, -1):
        assert data['data'][0]['id'] == i


def test_get_paginaton_limit_employees():
    response = requests.get(ENDPOINT + f'employees/?limit=1')
    data = response.json()

    assert response.status_code == 200

    assert data['count'] == 5

    assert len(data['data']) == 1


def test_get_paginaton_offset_employees():
    response = requests.get(ENDPOINT + f'employees/?offset=1')
    data = response.json()

    assert response.status_code == 200

    assert data['count'] == 5

    assert data['data'][0]['id'] == 2


def test_get_paginaton_limof_employees():
    response = requests.get(ENDPOINT + f'employees/?limit=1&offset=1')
    data = response.json()

    assert response.status_code == 200

    assert data['count'] == 5

    assert len(data['data']) == 1

    assert data['data'][0]['id'] == 2


def test_get_filter_employees():
    response_name = requests.get(ENDPOINT + f'employees/?name=Политыко%20Софья')
    data = response_name.json()

    assert response_name.status_code == 200

    assert data['count'] == 5

    for item in data['data']:
        assert item['name'] == 'Политыко Софья'


def test_get_ordering_employees():
    response_name = requests.get(ENDPOINT + f'employees/?ordering=age')
    data = response_name.json()

    assert response_name.status_code == 200

    assert data['count'] == 5

    assert data['data'] == sorted(data['data'], key=lambda d: d['age'])
