from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class TextBoxPage:
    def __int__(self, driver: WebDriver):
        self.url = "https://demoqa.com/text-box"
        self.driver = driver
        self.full_name_field = (By.ID, "userName")
        self.email_field = (By.ID, "userEmail")
        self.current_address_filed = (By.ID, "currentAddress")
        self.permanent_address_field = (By.ID, "permanentAddress")
        self.submit_button = (By.ID, "submit")
        self.result_fullname = (By.CSS_SELECTOR, "#name")
        self.result_email = (By.CSS_SELECTOR, "#email")
        self.result_curr_addr = (By.CSS_SELECTOR, "#currentAddress")
        self.result_perm_addr = (By.CSS_SELECTOR, "#permanentAddress")

    def open(self):
        self.driver.get(self.url)
        return self

    def clear_full_name_field(self) -> None:
        self.driver.find_element(*self.full_name_field).clear()
        return None

    def fill_full_name_field(self, text: str) -> None:
        self.driver.find_element(*self.full_name_field).send_keys(text)
        return None

    def clear_email_field(self) -> None:
        self.driver.find_element(*self.email_field).clear()
        return None

    def fill_email_field(self, text: str) -> None:
        self.driver.find_element(*self.email_field).send_keys(text)
        return None

    def clear_current_address_field(self) -> None:
        self.driver.find_element(*self.current_address_filed).clear()
        return None

    def fill_current_address_field(self, text: str) -> None:
        self.driver.find_element(*self.current_address_filed).send_keys(text)
        return None

    def clear_permanent_address_field(self) -> None:
        self.driver.find_element(*self.permanent_address_field).clear()
        return None

    def fill_permanent_address_field(self, text: str) -> None:
        self.driver.find_element(*self.permanent_address_field).send_keys(text)
        return None

    def click_submit_button(self) -> None:
        self.driver.find_element(*self.submit_button).click()
        return None

    def get_fullname(self) -> str:
        self.driver.find_element(*self.result_fullname).text

    def get_email(self) -> str:
        self.driver.find_element(*self.result_email).text

    def get_curr_addr(self) -> str:
        self.driver.find_element(*self.result_curr_addr).text

    def get_perm_addr(self) -> str:
        self.driver.find_element(*self.result_perm_addr).text
