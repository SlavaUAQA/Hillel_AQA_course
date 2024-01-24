# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
import requests


@pytest.fixture
def chrome():
    options = webdriver.ChromeOptions()
    options.add_argument("executable_path=/Users/viacheslavzakurenko/Downloads/chromedriver-mac-arm64/chromedriver")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
