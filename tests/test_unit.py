from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

def test_get_trainer():
    """
        Recuperation de la liste des Trainers
    """
    response = client.get("trainers/2640")
    assert response.status_code == 200
    assert response.json() == {"name": "Louille", "birthdate": "2002-05-13", "id":2640, "inventory": [], "pokemons": []}


def test_pokemons_random_different():
    """
        Recuperation de 3 pokemons aleatoires different
    """
    response = client.get("/pokemons/random/")
    assert response.status_code == 200
    assert response.json()[0]["id"] != response.json()[1]["id"] != response.json()[2]["id"]

def test_get_items():
    """
        Recuperation de la liste des items
    """
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json()[5] == {"name": "Super Mach", "description": "Fait monter de 10 niveaux un pokemon", "id": 5, "trainer_id": 2641}

def test_get_pokemons():
    """
        Recuperation de la liste des pokemons
    """
    response = client.get("/pokemons")
    assert response.status_code == 200
    assert response.json()[0] == {"api_id": 4, "custom_name": "Salameche", "id": 1491, "name": "charmander", "trainer_id": 2641}

def test_pokemon_battle():
    """
        Test de la fonction de combat
    """
    response = client.get("/pokemons/battle/1/4")
    assert response.status_code == 200
    assert response.json() == {"pokemonApiID": 1, "result": 9}

def test_pokemon_battle_draw():
    """
        Test de la fonction de combat si egalite
    """
    response = client.get("/pokemons/battle/4/4")
    assert response.status_code == 200
    assert response.json() == {"pokemonApiID": None, "result": 0}
