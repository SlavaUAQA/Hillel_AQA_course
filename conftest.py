# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
import requests


@pytest.fixture(scope="class")
def fixture_Chuck(request):
    response = requests.request(method="GET", url="https://api.chucknorris.io/jokes/search?query=first")
    status_code = response.status_code
    request.cls.response = response
    request.cls.status_code = status_code
    yield response, status_code

@pytest.fixture
def chrome():
    options = webdriver.ChromeOptions()
    options.add_argument("executable_path=C:\Program Files\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
