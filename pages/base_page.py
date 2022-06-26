
from selenium.common.exceptions import NoSuchElementException

from .locators import BasepageLocators

import logging
LOGGER = logging.getLogger()


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def go_to_elements_page(self):
        link = self.browser.find_element(*BasepageLocators.ELEMENTS_PAGE)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", link)
        link.click()

    def go_to_forms_page(self):
        link = self.browser.find_element(*BasepageLocators.FORMS_PAGE)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", link)
        link.click()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
