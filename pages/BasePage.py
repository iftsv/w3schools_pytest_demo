from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException

"""
This class is the parent of all pages
It contains all the generic methods and utilities for all the pages
"""


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator: object) -> object:
        WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(by_locator)).click()

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(by_locator))
        return element.text

    def get_sql_result_table(self, by_table_locator):
        try:
            return WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(by_table_locator))
        except TimeoutException as ex:
            print("Exception has been thrown. " + str(ex))
