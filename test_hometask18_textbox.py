import pytest
from selenium_tasks.hometask_18_textbox import TextBoxPage
from selenium.webdriver.support.ui import WebDriverWait
import time


class TestTextBoxPage:
    def test_email_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_email_field("slavaUAQA@gmail.com")
        page.scroll_down()
        page.click_submit_button()
        email_field = page.get_email()
        assert email_field.replace("Email:", "") == "slavaUAQA@gmail.com"

    def test_curr_addr_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_current_address_field("Krakow")
        page.scroll_down()
        page.click_submit_button()
        time.sleep(5)
        curr_addr_field = page.get_curr_addr()
        assert curr_addr_field.replace("Current Address :", "") == "Krakow"

    def test_perm_addr_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_permanent_address_field("Kharkiv")
        page.scroll_down()
        page.click_submit_button()
        time.sleep(10)
        perm_addr_field = page.get_perm_addr()
        assert perm_addr_field.replace("Permananet Address :", "") == "Kharkiv"    
