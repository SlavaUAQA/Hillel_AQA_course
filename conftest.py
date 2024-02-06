# -*- coding: utf-8 -*-
import pytest
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

@pytest.fixture
def firefox():
    options = Options()
    driver = Firefox(executable_path="/Users/viacheslavzakurenko/PycharmProjects/Hillel_AQA_course/selenium_tasks/geckodriver")
    yield driver
    driver.quit()
