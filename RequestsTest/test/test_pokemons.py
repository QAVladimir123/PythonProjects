import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'ce3965733d527e392ccbfd3519a2429e'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
TRANIER_ID = 17443
TRAINER_NAME = 'Python'
def test_status_code():
    response = requests.get(url=f'{URL}/pokemons',params= {'trainer_id' : TRANIER_ID})
    assert response.status_code == 200

def test_part_of_respons():
    response_get = requests.get(url=f'{URL}/pokemons',params= {'trainer_id' : TRANIER_ID})
    assert response_get.json()["data"][0]["name"] == 'Vorsa'

def test_trainer_name():
    trainer_get = requests.get(url=f'{URL}/trainers',params= {'trainer_id' : TRANIER_ID})
    assert trainer_get.json()["data"][0]["trainer_name"] == 'Python'