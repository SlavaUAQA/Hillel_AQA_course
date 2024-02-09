import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec

from selenium_tasks.hometask20_DynamicPropertiesPage import DynamicPropertiesPage

class TestButtonsWait:
    def test_enable_button(self, firefox):
        self.driver = firefox
        page = DynamicPropertiesPage(firefox)
        page.open()
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(page.enable_button))
        page.get_agree_to_use_data().click()
        page.get_enable_button().click()
        assert page.get_enable_button().is_enabled()

    def test_color_change_button(self, firefox):
        self.driver = firefox
        page = DynamicPropertiesPage(firefox)
        page.open()
        WebDriverWait(self.driver, 10).until(ec.text_to_be_present_in_element_attribute(page.color_change_button, "class", "text-danger"))
        page.get_agree_to_use_data().click()
        page.get_color_change_button().click()
        assert "text-danger" in page.get_color_change_button().get_attribute("class")

    def test_get_visible_button(self, firefox):
        self.driver = firefox
        page = DynamicPropertiesPage(firefox)
        page.open()
        WebDriverWait(self.driver, 10).until(ec.visibility_of_all_elements_located(page.visible_after_button))
        page.get_agree_to_use_data().click()
        page.get_visible_after_button()
        assert page.get_visible_after_button().is_displayed()
