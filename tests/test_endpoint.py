from app import app, get_db
from fastapi.testclient import TestClient
from unittest.mock import Mock, patch

client = TestClient(app)

def test_endpoint_setdb():
    mock_task = Mock()
    mock_task.id = "123"

    with patch("app.set_database.delay", return_value=mock_task):
        response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data == {"task_id": "123", "message": "Setting DB."}

def test_endpoint_status():
    mock_task = Mock()
    mock_task.status = "SUCCESS"

    with patch("app.AsyncResult", return_value=mock_task):
        response = client.get("/status/123")

    assert response.status_code ==  200

    assert response.json() == {"status": "SUCCESS"}

def test_endpoint_pokemon():
    mock_pokemon = Mock()
    mock_pokemon.id = 1
    mock_pokemon.name = "bulbasaur"
    mock_pokemon.height = 7
    mock_pokemon.weight = 69
    mock_pokemon.types = ["grass", "poison"]
    mock_pokemon.sprites = "sprite_url"

    mock_db = Mock()
    mock_db.query.return_value.offset.return_value.limit.return_value.all.return_value = [mock_pokemon]

    def override_get_db():
        return mock_db

    app.dependency_overrides[get_db] = override_get_db

    try:
        response = client.get("/pokemon")

        assert response.status_code == 200

        assert response.json() == {
            "pokemonList": [
                "Pokemon: ",
                {
                    "id": 1,
                    "name": "bulbasaur",
                    "height": 7,
                    "weight": 69,
                    "types": ["grass", "poison"],
                    "sprites": "sprite_url"
                }
            ]
        }
    finally:
        app.dependency_overrides.clear()

def test_endpoint_per_pokemon():
    mock_pokemon = Mock()
    mock_pokemon.id = 1
    mock_pokemon.name = "bulbasaur"
    mock_pokemon.height = 7
    mock_pokemon.weight = 69
    mock_pokemon.types = ["grass", "poison"]
    mock_pokemon.sprites = "sprite_url"

    mock_db = Mock()
    mock_db.query.return_value.filter.return_value.first.return_value = mock_pokemon

    def override_get_db():
        return mock_db

    app.dependency_overrides[get_db] = override_get_db

    try:
        response = client.get("/pokemon/1")

        assert response.status_code == 200

        assert response.json() == {
                "id": 1,
                "name": "bulbasaur",
                "height": 7,
                "weight": 69,
                "types": ["grass", "poison"],
                "sprites": "sprite_url"
            }
    finally:
        app.dependency_overrides.clear()
