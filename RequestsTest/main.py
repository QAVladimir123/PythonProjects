import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'ce3965733d527e392ccbfd3519a2429e'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "string",
    "password": "string"
}

body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}
body_change = {
    "pokemon_id": "128242",
    "name": "Vorsa",
    "photo_id": 7
}

body_pokeball = {
    "pokemon_id": "9"
}


'''response = requests.post(url=f'{URL}/trainers/reg', headers=HEADER, json=body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url=f'{URL}/trainers/confirm_email', headers= HEADER, json= body_confirmation)
print(response_confirmation.text)'''


'''response_create = requests.post(url= f'{URL}/pokemons', headers= HEADER, json= body_create)
print(response_create.text)

message = response_create.json()['message']
print(message)'''

'''response_change = requests.put(url= f'{URL}/pokemons',headers= HEADER, json= body_change)
print(response_change.text)

message = response_change.json()['message']
print(message)'''

response_pokeball = requests.post(url= f'{URL}/trainers/add_pokeball',headers= HEADER, json= body_change)
print(response_pokeball.text)

message = response_pokeball.json()['message']
print(message)