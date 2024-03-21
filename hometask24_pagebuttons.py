from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class PageButtons:
    URL = "https://demoqa.com/buttons"

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.button_doubleclick_loc = (By.ID, "doubleClickBtn")
        self.button_right_click_loc = (By.CSS_SELECTOR, "#rightClickBtn")
        self.button_dynamic_id_loc = (By.XPATH, '//button[.="Click Me"]')
        self.button_doubleclick_message_loc = (By.ID, "doubleClickMessage")
        self.button_right_click_message_loc = (By.CSS_SELECTOR, "#rightClickMessage")
        self.button_dynamic_id_click_message_loc = (By.ID, "dynamicClickMessage")

    def open(self):
        self.driver.get(self.URL)
        return self

    def doubleclick_button(self):
        button = self.driver.find_element(*self.button_doubleclick_loc)
        return button

    def right_click_button(self):
        button = self.driver.find_element(*self.button_right_click_loc)
        return button

    def dynamic_id_click_button(self):
        button = self.driver.find_element(*self.button_dynamic_id_loc)
        return button

    def get_button_doubleclick_message(self) -> str:
        return self.driver.find_element(*self.button_doubleclick_message_loc).text

    def get_button_right_click_message(self) -> str:
        return self.driver.find_element(*self.button_right_click_message_loc).text

    def get_button_dynamic_id_click_message(self) -> str:
        return self.driver.find_element(*self.button_dynamic_id_click_message_loc).text

    def maximize_window(self):
        self.driver.maximize_window()
