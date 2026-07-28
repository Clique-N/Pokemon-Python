from app import app, get_db
from fastapi.testclient import TestClient
from unittest.mock import Mock, patch

client = TestClient(app)

def test_page_successfully():
    mock_pokemon1 = Mock()
    mock_pokemon1.id = 1
    mock_pokemon1.name = "bulbasaur"
    mock_pokemon1.height = 7
    mock_pokemon1.weight = 69
    mock_pokemon1.types = ["grass", "poison"]
    mock_pokemon1.sprites = "sprite_url"

    mock_pokemon2 = Mock()
    mock_pokemon2.id = 2
    mock_pokemon2.name = "ivysaur"
    mock_pokemon2.height = 10
    mock_pokemon2.weight = 100
    mock_pokemon2.types = ["grass", "poison"]
    mock_pokemon2.sprites = "sprite_url"

    mock_db = Mock()
    mock_db.query.return_value.offset.return_value.limit.return_value.all.return_value = [mock_pokemon1, mock_pokemon2]

    def override_get_db():
        return mock_db

    app.dependency_overrides[get_db] = override_get_db

    try:
        response = client.get("/pokemon?page=1&limit=2")

        assert response.status_code == 200

        data = response.json()

        assert len(data["pokemonList"]) == 3
        mock_db.query.return_value.offset.assert_called_once_with(0)
        mock_db.query.return_value.offset.return_value.limit.assert_called_once_with(2)

    finally:
        app.dependency_overrides.clear()

def test_page_invalid():
    response = client.get("/pokemon?page=0&limit=10")

    assert response.status_code == 400

    assert response.json() == {"detail": "Page or limit with invalid values."}

def test_page_not_found():
    mock_db = Mock()

    mock_db.query.return_value.offset.return_value.limit.return_value.all.return_value = []

    def override_get_db():
        return mock_db

    app.dependency_overrides[get_db] = override_get_db

    try:
        response = client.get("/pokemon?page=100&limit=10")

        assert response.status_code ==  404

        assert response.json() == {"detail": "Pokemon not found!"}

    finally:
        app.dependency_overrides.clear()

def test_pokemon_not_found():
    mock_db = Mock()

    mock_db.query.return_value.filter.return_value.first.return_value = []

    def override_get_db():
        return mock_db

    app.dependency_overrides[get_db] = override_get_db

    try:
        response = client.get("/pokemon/160")

        assert response.status_code ==  404

        assert response.json() == {"detail": "Pokemon not found!"}

    finally:
        app.dependency_overrides.clear()