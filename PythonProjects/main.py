import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'e65e889591dca986abbd30e0aa668c1c'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
body_registration = {
    "trainer_token": TOKEN,
    "email": "i@dgribenchenko.ru",
    "password": "Grebchik1992@"
}
body_confirmation = {
    "trainer_token": TOKEN
}
body_create = {
    "name": "Бурбон",
    "photo_id": 1
}
body_change = {
    "pokemon_id": "143996",
    "name": "Принц",
    "photo_id": 2
}
body_catch = { 
    "pokemon_id": "143996"
}

'''response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)'''

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)