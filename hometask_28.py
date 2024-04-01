from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class PageCheckbox:
    URL = "https://demoqa.com/checkbox"

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.button_home_expand_loc = (By.CSS_SELECTOR, "#tree-node > ol > li > span > button > svg")
        self.button_desctop_expand_loc = (
        By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(1) > span > button > svg")
        self.button_documents_expand_loc = (
        By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(2) > span > button > svg")
        self.button_offices_expand_loc = (
        By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(2) > ol > li:nth-child(2) > span > button > svg")
        self.ckeckbox_commands_loc = (By.CSS_SELECTOR,
                                      "#tree-node > ol > li > ol > li:nth-child(1) > ol > li:nth-child(2) > span > label > span.rct-checkbox > svg")
        self.ckeckbox_general_loc = (By.CSS_SELECTOR,
                                     "#tree-node > ol > li > ol > li:nth-child(2) > ol > li:nth-child(2) > ol > li:nth-child(4) > span > label > span.rct-checkbox > svg")
        self.button_expand_all_loc = (
        By.CSS_SELECTOR, "#tree-node > div > button.rct-option.rct-option-expand-all > svg")

    def open(self):
        self.driver.get(self.URL)
        return self

    def commands_checkbox(self):
        checkbox = self.driver.find_element(*self.ckeckbox_commands_loc)
        return checkbox

    def general_checkbox(self):
        checkbox = self.driver.find_element(*self.ckeckbox_general_loc)
        return checkbox

    def button_expand_all(self):
        button = self.driver.find_element(*self.button_expand_all_loc)
        return button

    def scroll_to_general_checkbox(self):
        element = self.driver.find_element(*self.ckeckbox_general_loc)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def scroll_to_commands_checkbox(self):
        element = self.driver.find_element(*self.ckeckbox_commands_loc)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
