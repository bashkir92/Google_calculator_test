from BasePage import BasePage
from selenium.webdriver.common.by import By

class GoogleLocators:


    LOCATOR_GOOGLE_SEARCH = (By.NAME, "q")
    LOCATOR_GOOGLE_SEARCH_BUTTON = (By.XPATH, '//*[@name="btnK"]')
    LOCATOR_GOOGLE_BUTTON_ONE = (By.XPATH, '//*[@jsname="N10B9"]')
    LOCATOR_GOOGLE_BUTTON_TWO = (By.XPATH, '//*[@jsname="lVjWed"]')
    LOCATOR_GOOGLE_BUTTON_THREE = (By.XPATH, '//*[@jsname="KN1kY"]')
    LOCATOR_GOOGLE_BUTTON_MULT = (By.XPATH, '//*[@jsname="YovRWb"]')
    LOCATOR_GOOGLE_BUTTON_MINUS = (By.XPATH, '//*[@jsname="pPHzQc"]')
    LOCATOR_GOOGLE_BUTTON_PLUS = (By.XPATH, '//*[@jsname="XSr6wc"]')
    LOCATOR_GOOGLE_BUTTON_EQUALS = (By.XPATH, '//*[@jsname="Pt8tGc"]')
    LOCATOR_GOOGLE_LINE_RESULT = (By.XPATH, '//*[@id="cwos"]')
    LOCATOR_GOOGLE_LINE_MEMORY = (By.XPATH, '//*[@jsname="ubtiRe"]')


class Search(BasePage):


    def enter_word(self, word):
        search = self.find_element(GoogleLocators.LOCATOR_GOOGLE_SEARCH)
        search.click()
        search.send_keys(word)
        return search

    def click_on_the_search_button(self):
        return self.find_element(GoogleLocators.LOCATOR_GOOGLE_SEARCH_BUTTON).click()

    def click_on_one(self):
        return self.find_element(GoogleLocators.LOCATOR_GOOGLE_BUTTON_ONE).click()

    def click_on_two(self):
        return self.find_element(GoogleLocators.LOCATOR_GOOGLE_BUTTON_TWO).click()

    def click_on_three(self):
        return self.find_element(GoogleLocators.LOCATOR_GOOGLE_BUTTON_THREE).click()

    def click_on_mult(self):
        return self.find_element(GoogleLocators.LOCATOR_GOOGLE_BUTTON_MULT).click()

    def click_on_minus(self):
        return self.find_element(GoogleLocators.LOCATOR_GOOGLE_BUTTON_MINUS).click()

    def click_on_plus(self):
        return self.find_element(GoogleLocators.LOCATOR_GOOGLE_BUTTON_PLUS).click()

    def click_on_equals(self):
        return self.find_element(GoogleLocators.LOCATOR_GOOGLE_BUTTON_EQUALS).click()

    def line_result(self):
        return self.find_element(GoogleLocators.LOCATOR_GOOGLE_LINE_RESULT).text

    def line_memory(self):
        return self.find_element(GoogleLocators.LOCATOR_GOOGLE_LINE_MEMORY).text
