from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class VringeMainPage:
    URL = "https://vringe.com/"
  
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.header_main_button = (By.CSS_SELECTOR, "body > div.width > header > ul.menu > li.selected > a")
        self.header_mma_button = (By.CSS_SELECTOR, "body > div.width > header > ul.menu > li:nth-child(2) > a")
        self.header_p4p_button = (By.CSS_SELECTOR, "body > div.width > header > ul.menu > li:nth-child(3) > a")
        self.header_video_button = (By.CSS_SELECTOR, "body > div.width > header > ul.menu > li:nth-child(4) > a")
        self.header_photo_button = (By.CSS_SELECTOR, "body > div.width > header > ul.menu > li:nth-child(5) > a")
        self.header_news_button = (By.XPATH, "/html/body/div[1]/header/ul[2]/li[1]/a")
        self.header_exclusive_button = (By.XPATH, "/html/body/div[1]/header/ul[2]/li[3]/a")
        self.header_prediction_button = (By.XPATH, "/html/body/div[1]/header/ul[2]/li[5]/a")
        self.header_ratings_button = (By.XPATH, "/html/body/div[1]/header/ul[2]/li[7]/a")
        self.header_top10_button = (By.XPATH, "/html/body/div[1]/header/ul[2]/li[9]/a")
