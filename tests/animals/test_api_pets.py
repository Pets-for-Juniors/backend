import requests

ENDPOINT = 'http://127.0.0.1:8000/api/pets'
COUNT = 20

def test_can_call_endpoint():
    response = requests.get(f'{ENDPOINT}/')
    assert response.status_code == successful_status_code


def test_can_call_endpoint_id_cards():
    i = 1
    while i < 6:
        response = requests.get(f'{ENDPOINT}/{i}/')
        assert response.status_code == successful_status_code
        get_data = response.json()
        assert get_data['id'] == i
        i += 1


def test_can_call_endpoint_type_dog():
    response = requests.get(f'{ENDPOINT}/?type=dog')
    assert response.status_code == successful_status_code
    get_data_type = response.json()
    assert get_data_type['count'] == COUNT
    data = get_data_type['data']
    for el in data:
        assert el['type'] == 'dog'


def test_can_call_endpoint_sex_female():
    response = requests.get(f'{ENDPOINT}/?sex=female')
    assert response.status_code == successful_status_code
    get_data_type = response.json()
    assert get_data_type['count'] == COUNT
    data = get_data_type['data']
    for el in data:
        assert el['sex'] == 'female'


def test_can_call_endpoint_age_4():
    age = 4
    response = requests.get(f'{ENDPOINT}/?age={age}')
    assert response.status_code == successful_status_code
    get_data_type = response.json()
    assert get_data_type['count'] == COUNT
    data = get_data_type['data']
    for el in data:
        assert el['age'] == age


def test_can_call_endpoint_breed():
    response = requests.get(f'{ENDPOINT}/?breed=Хаски')
    assert response.status_code == successful_status_code
    get_data_type = response.json()
    assert get_data_type['count'] == COUNT
    data = get_data_type['data']
    for el in data:
        assert el['breed'] == 'Хаски'


def test_can_call_endpoint_pagination_limit():
    limit = 5
    response = requests.get(f'{ENDPOINT}/?limit={limit}')
    assert response.status_code == successful_status_code
    get_data_type = response.json()
    assert get_data_type['count'] == COUNT
    limit = len(get_data_type['data'])
    assert limit == limit


def test_can_call_endpoint_pagination_offset():
    offset = 4
    response = requests.get(f'{ENDPOINT}/?offset={offset}')
    assert response.status_code == successful_status_code
    get_data_type = response.json()
    assert get_data_type['count'] == COUNT
    data = get_data_type['data']
    assert data[0]['id'] == offset + 1


def test_can_call_endpoint_ordering():
    response = requests.get(f'{ENDPOINT}/?ordering=age')
    assert response.status_code == successful_status_code
    get_data_type = response.json()
    assert get_data_type['count'] == COUNT
    data = get_data_type['data']
    ordering_data = sorted(data, key=lambda d: d['age'])
    assert ordering_data == data
