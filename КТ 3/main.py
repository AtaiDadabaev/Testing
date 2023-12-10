import pytest
import requests
import json

BASE_URL = "https://petstore.swagger.io/v2/"
HEADERS = {"Content-Type": "application/json"}

@pytest.fixture
def pet_data():
    return {
        "id": 0,
        "category": {"id": 0, "name": "string"},
        "name": "Atai",
        "photoUrls": ["string"],
        "tags": [{"id": 0, "name": "string"}],
        "status": "available",
    }

@pytest.fixture
def updated_pet_data():
    return {
        "id": 10,
        "category": {"id": 0, "name": "string"},
        "name": "Atai_Cool_7",
        "photoUrls": ["string"],
        "tags": [{"id": 0, "name": "string"}],
        "status": "available",
    }

def test_add_pet(pet_data):
    response = requests.post(BASE_URL + "pet", headers=HEADERS, json=pet_data)
    assert response.status_code == 200
    assert response.json()["name"] == pet_data["name"]

def test_get_pet():
    response = requests.get(BASE_URL + "pet/5")
    assert response.status_code == 200
    assert "name" in response.json()

def test_update_pet(updated_pet_data):
    response = requests.put(BASE_URL + "pet", headers=HEADERS, json=updated_pet_data)
    assert response.status_code == 200

def test_delete_pet():
    response = requests.delete(BASE_URL + "pet/5")
    assert response.status_code == 200

def test_add_updated_pet(updated_pet_data):
    response = requests.post(BASE_URL + "pet", headers=HEADERS, json=updated_pet_data)
    assert response.status_code == 200
    assert response.json()["name"] == updated_pet_data["name"]
