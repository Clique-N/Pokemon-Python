import requests

BASE_URL = "https://pokeapi.co/api/v2/pokemon"

def get_pokemon(pokemon_id):
    response = requests.get(f"{BASE_URL}/{pokemon_id}")

    if response.status_code == 200:
        return response.json()

    return None