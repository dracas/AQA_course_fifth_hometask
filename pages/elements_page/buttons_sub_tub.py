import logging
from selenium.webdriver.common.action_chains import ActionChains
from .elements_page import ElementsPage
from ..locators import ElementsPageLocators
LOGGER = logging.getLogger()


class ButtonsSubTub(ElementsPage):
    def click_on_click_me_button(self):
        link = self.browser.find_element(*ElementsPageLocators.BUTTONS_SUB_TUB_CLICK_BTN)
        link.click()

    def click_on_double_click_me_button(self):
        link = self.browser.find_element(*ElementsPageLocators.BUTTONS_SUB_TUB_DOUBLE_CLICK_BTN)
        link.click()

    def double_click_on_button(self):
        link = self.browser.find_element(*ElementsPageLocators.BUTTONS_SUB_TUB_DOUBLE_CLICK_BTN)
        action = ActionChains(self.browser)
        action.double_click(link)
        action.perform()

    def should_be_needed_message_after_click_to_click_me_button(self):
        assert self.is_element_present(*ElementsPageLocators.BUTTONS_SUB_TUB_DYNAMIC_CLICK_MESSAGE), \
            "Message after click to click me button is missing on Elements page, buttons sub-tub"

    def should_be_needed_message_after_click_to_double_click_me_button(self):
        assert self.is_element_present(*ElementsPageLocators.BUTTONS_SUB_TUB_DOUBLE_CLICK_MESSAGE), \
            "Message after click to double click me button is missing on Elements page, buttons sub-tub"
