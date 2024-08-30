import requests

ENDPOINT = 'http://127.0.0.1:8000/api/pets'


def test_can_call_endpoint():
    response = requests.get(f'{ENDPOINT}/')
    assert response.status_code == 200


def test_can_call_endpoint_id_cards():
    i = 1
    while i < 6:
        response = requests.get(f'{ENDPOINT}/{i}/')
        get_data = response.json()
        assert get_data['id'] == i
        i += 1


def test_can_call_endpoint_type_dog():
    response = requests.get(f'{ENDPOINT}/?type=dog')
    get_data_type = response.json()
    data = get_data_type['data']
    for el in data:
        assert el['type'] == 'dog'


def test_can_call_endpoint_sex_female():
    response = requests.get(f'{ENDPOINT}/?sex=female')
    get_data_type = response.json()
    data = get_data_type['data']
    for el in data:
        assert el['sex'] == 'female'


def test_can_call_endpoint_age_4():
    age = 4
    response = requests.get(f'{ENDPOINT}/?age={age}')
    get_data_type = response.json()
    data = get_data_type['data']
    for el in data:
        assert el['age'] == age


def test_can_call_endpoint_breed():
    response = requests.get(f'{ENDPOINT}/?breed=Хаски')
    get_data_type = response.json()
    data = get_data_type['data']
    for el in data:
        assert el['breed'] == 'Хаски'


def test_can_call_endpoint_pagination_limit():
    limit = 5
    response = requests.get(f'{ENDPOINT}/?limit={limit}')
    get_data_type = response.json()
    limit = len(get_data_type['data'])
    assert limit == limit


def test_can_call_endpoint_pagination_offset():
    offset = 4
    response = requests.get(f'{ENDPOINT}/?offset={offset}')
    get_data_type = response.json()
    data = get_data_type['data']
    assert data[0]['id'] == offset + 1


def test_can_call_endpoint_ordering():
    response = requests.get(f'{ENDPOINT}/?ordering=age')
    get_data_type = response.json()
    data = get_data_type['data']
    ordering_data = sorted(data, key=lambda d: d['age'])
    assert ordering_data == data



