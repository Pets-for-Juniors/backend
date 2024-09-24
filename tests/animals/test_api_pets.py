import pytest
import requests

from tests.test_constants import successful_status_code
from tests.animals.test_animal_constans import (breed_list, age_list, limit_list, offset_list, id_list,
                                  type_list, gender_list)

ENDPOINT = 'http://127.0.0.1:8000/api/pets'
COUNT = 20

def test_can_call_endpoint():
    response = requests.get(f'{ENDPOINT}/')
    assert response.status_code == successful_status_code


@pytest.mark.parametrize('id', id_list)
def test_can_call_endpoint_id_cards(id):
    response = requests.get(f'{ENDPOINT}/{id}/')
    assert response.status_code == successful_status_code
    get_data = response.json()
    assert get_data['id'] == id


@pytest.mark.parametrize('type', type_list)
def test_can_call_endpoint_type_dog(type):
    response = requests.get(f'{ENDPOINT}/?type={type}')
    assert response.status_code == successful_status_code
    get_data = response.json()
    assert get_data['count'] == 11 if type == 'Собака' else 9
    data = get_data['results']
    for el in data:
        assert el['type'] == type


@pytest.mark.parametrize('gender', gender_list)
def test_can_call_endpoint_sex_female(gender):
    response = requests.get(f'{ENDPOINT}/?gender={gender}')
    assert response.status_code == successful_status_code
    get_data = response.json()
    assert get_data['count'] == 13 if type == 'Мужской' else 7
    data = get_data['results']
    for el in data:
        assert el['gender'] == gender


@pytest.mark.parametrize('age', age_list)
def test_can_call_endpoint_age_4(age):
    response = requests.get(f'{ENDPOINT}/?age={age}')
    assert response.status_code == successful_status_code
    get_data = response.json()
    assert get_data['count'] == len(get_data['results'])
    data = get_data['results']
    for el in data:
        assert el['age'] == age


@pytest.mark.parametrize('breed', breed_list)
def test_can_call_endpoint_breed(breed):
    response = requests.get(f'{ENDPOINT}/?breed={breed}')
    assert response.status_code == successful_status_code
    get_data = response.json()
    assert get_data['count'] == len(get_data['results'])
    data = get_data['results']
    for el in data:
        assert el['breed'] == breed


@pytest.mark.parametrize('limit', limit_list)
def test_can_call_endpoint_pagination_limit(limit):
    response = requests.get(f'{ENDPOINT}/?limit={limit}')
    assert response.status_code == successful_status_code
    get_data = response.json()
    limit_data = len(get_data['results'])
    assert get_data['count'] == COUNT
    assert limit_data == limit


@pytest.mark.parametrize('offset', offset_list)
def test_can_call_endpoint_pagination_offset(offset):
    response = requests.get(f'{ENDPOINT}/?offset={offset}')
    assert response.status_code == successful_status_code
    get_data = response.json()
    assert get_data['count'] == COUNT
    data = get_data['results']
    assert data[0]['id'] == offset + 1


def test_can_call_endpoint_ordering():
    response = requests.get(f'{ENDPOINT}/?ordering=age')
    assert response.status_code == successful_status_code
    get_data = response.json()
    assert get_data['count'] == COUNT
    data = get_data['results']
    ordering_data = sorted(data, key=lambda d: d['age'])
    assert ordering_data == data
