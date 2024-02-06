from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox
class ElementsPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/elements"
        self.element_categories = By.XPATH, "//div[contains(@class, show)]//li"

    def open(self):
        self.driver.get(self.url)
        return self

    def get_elements_categories(self):
        categories = [cat.text for cat in self.driver.find_elements(*self.element_categories)]
        return categories

    def close(self):
        self.driver.close()
        return self

def obj1():
    a = ElementsPage(webdriver.Firefox())
    a.open()
    for i in a.get_elements_categories():
        print(i)
    print(len(a.get_elements_categories()))

obj1()
