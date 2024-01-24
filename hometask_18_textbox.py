from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class TextBoxPage:
    def __init__(self, driver: WebDriver):
        self.url = "https://demoqa.com/text-box"
        self.driver = driver
        self.full_name_field = (By.ID, "userName")
        self.email_field = (By.CSS_SELECTOR, "#userEmail")
        self.current_address_filed = (
        By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[3]/div[2]/textarea")
        self.permanent_address_field = (
        By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[4]/div[2]/textarea")
        self.submit_button = (By.ID, "submit")
        self.result_fullname = (By.CSS_SELECTOR, "#name")
        self.result_email = (By.CSS_SELECTOR, "#email")
        self.result_curr_addr = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[6]/div/p")
        self.result_perm_addr = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[6]/div/p")

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
        return self.driver.find_element(*self.result_fullname).text

    def get_email(self) -> str:
        return self.driver.find_element(*self.result_email).text

    def get_curr_addr(self) -> str:
        return self.driver.find_element(*self.result_curr_addr).text

    def get_perm_addr(self) -> str:
        return self.driver.find_element(*self.result_perm_addr).text

    def scroll_down(self) -> None:
        self.driver.execute_script("window.scrollBy(0, 500);")
