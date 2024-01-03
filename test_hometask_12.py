import requests
import pytest


def test_image():
    URL = "https://api.chucknorris.io/jokes/random"
    response = requests.get(URL)
    icon_url = response.json().get('icon_url')
    assert icon_url.endswith(".png")


def test_image_value():
    URL = "https://api.chucknorris.io/jokes/random"
    response = requests.get(URL)
    icon_url = response.json().get('icon_url')
    assert icon_url is not None


def test_value_key():
    URL = "https://api.chucknorris.io/jokes/random"
    response = requests.get(URL)
    assert response.json().get('value')


def test_value_key_1():
    URL = "https://api.chucknorris.io/jokes/random"
    response = requests.get(URL)
    assert response.json().get('value')[:] is not None


@pytest.mark.usefixtures("fixture_Chuck")
class TestChuck:
    def test_status_code(self):
        assert self.status_code == 200

    def test_chuck_query(self):
        query = "first"
        URL = f"https://api.chucknorris.io/jokes/search?query={query}"
        response = requests.get(URL)
        jokes = response.json()['result']
        assert any(
            query.lower() in joke.get('value', '').lower() for joke in jokes), f"No jokes contain the word '{query}'"

    def test_total_amount(self):
        query = "avenger"
        URL = f"https://api.chucknorris.io/jokes/search?query={query}"
        response = requests.get(URL)
        assert response.json()['total'] > 0, f"total amount of jokes with chosen word is {response.json()['total']}"
        print(f"total amount of jokes with chosen word is {response.json()['total']}")
