from unittest.mock import Mock, patch
from src.pokeapi import get_pokemon
from src.repository import save_pokemon

@patch("src.pokeapi.requests.get")
def test_get_pokemon(mock_get):
    mock_response = Mock()

    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "bulbasaur"}

    mock_get.return_value = mock_response

    result = get_pokemon(1)

    assert result["name"] == "bulbasaur"
    assert result["id"] == 1

@patch("src.pokeapi.requests.get")
def test_get_pokemon_not_found(mock_get):
    mock_response = Mock()

    mock_response.status_code = 404

    mock_get.return_value = mock_response

    result = get_pokemon(500)

    assert result is None

def test_save_pokemon():
    mock_pokemon = Mock()
    pokemon_data = {
        "id": 25,
        "name": "pikachu",
        "height": 4,
        "weight": 60,
        "types": [{"type":{
            "name": "eletric"
        }}],
        "sprites": {"front_default": "pikachu.png"}
    }

    save_pokemon(mock_pokemon, pokemon_data)

    mock_pokemon.add.assert_called_once()
    mock_pokemon.commit.assert_called_once()