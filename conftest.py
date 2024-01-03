import pytest
import requests


@pytest.fixture(scope="class")
def fixture_Chuck(request):
    response = requests.request(method="GET", url="https://api.chucknorris.io/jokes/search?query=first")
    status_code = response.status_code
    request.cls.response = response
    request.cls.status_code = status_code
    yield response, status_code
