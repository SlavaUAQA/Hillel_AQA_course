import pytest
import requests
import sqlite3


@pytest.fixture(scope="class")
def fixture_Chuck(request):
    response = requests.request(method="GET", url="https://api.chucknorris.io/jokes/search?query=first")
    status_code = response.status_code
    request.cls.response = response
    request.cls.status_code = status_code
    yield response, status_code

@pytest.fixture(scope="function")
def fixture_sql():
    connection = sqlite3.connect("hometask_sport.db")
    cursor = connection.cursor()
    yield cursor
    cursor.close()
    connection.close()
