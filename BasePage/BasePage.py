import Config

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.url = Config.url

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver,time).until(EC.visibility_of_element_located(locator), message=f"Не удается найти элемент по локатору {locator}")

    def go_to_site(self):
        return self.driver.get(self.url)