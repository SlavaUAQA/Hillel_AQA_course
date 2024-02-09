from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

class DynamicPropertiesPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = "https://demoqa.com/dynamic-properties"
        self.enable_button = (By.CSS_SELECTOR, "#enableAfter")
        self.color_change_button = (By.CSS_SELECTOR, "#colorChange")
        self.visible_after_button = (By.CSS_SELECTOR, "#visibleAfter")
        self.agree_to_use_data = (By.CSS_SELECTOR, ".fc-cta-consent > p:nth-child(2)")

    def open(self):
        self.driver.get(self.url)
        return self

    def get_enable_button(self) -> WebElement:
        button = self.driver.find_element(*self.enable_button)
        return button

    def get_color_change_button(self) -> WebElement:
        button = self.driver.find_element(*self.color_change_button)
        return button

    def get_visible_after_button(self) -> WebElement:
        button = self.driver.find_element(*self.visible_after_button)
        return button

    def get_agree_to_use_data(self) -> WebElement:
        button = self.driver.find_element(*self.agree_to_use_data)
        return button
