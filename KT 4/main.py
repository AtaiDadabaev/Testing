import requests
import pytest
import json

BASE_URL = "https://dog.ceo/api"

def get_response(url):
    response = requests.get(url)
    return response

@pytest.fixture
def url_fixture(request):
    return request.param

@pytest.mark.parametrize("url_fixture", [
    f"{BASE_URL}/breeds/list/all",
    f"{BASE_URL}/breeds/image/random",
    f"{BASE_URL}/breed/hound/list",
    f"{BASE_URL}/breed/hound/afghan/images",
    f"{BASE_URL}/breed/hound/afghan/images/random"
], indirect=True)

def test_dog_api(url_fixture):
    response = get_response(url_fixture)

    assert response.status_code == 200    
    json_data = response.json()

    assert "message" in json_data

    message_value_type = type(json_data["message"])
    assert message_value_type in [list, str, dict]

    assert bool(json_data["message"])
