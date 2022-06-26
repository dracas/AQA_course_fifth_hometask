from ..base_page import BasePage
from ..locators import ElementsPageLocators


class ElementsPage(BasePage):
    def go_to_text_box_sub_tub(self):
        link = self.browser.find_element(*ElementsPageLocators.TEXT_BOX_SUB_TUB)
        link.click()

    def go_to_check_box_sub_tub(self):
        link = self.browser.find_element(*ElementsPageLocators.CHECK_BOX_SUB_TUB)
        link.click()

    def go_to_radio_button_sub_tub(self):
        link = self.browser.find_element(*ElementsPageLocators.RADIO_BUTTON_SUB_TUB)
        link.click()

    def go_to_buttons_sub_tub(self):
        link = self.browser.find_element(*ElementsPageLocators.BUTTONS_SUB_TUB)
        link.click()
