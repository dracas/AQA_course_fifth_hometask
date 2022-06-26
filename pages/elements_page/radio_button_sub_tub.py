import logging
from .elements_page import ElementsPage
from ..locators import ElementsPageLocators
from ...test_data.texts import RADIO_BUTTON_SUCCESSFUL_MESSAGE
LOGGER = logging.getLogger()


class RadioButtonSubTub(ElementsPage):
    def click_on_button(self, button):
        if button == 'Yes':
            link = self.browser.find_element(*ElementsPageLocators.RADIO_BUTTON_SUB_TUB_YES_BTN)
            link.click()
        elif button == 'Impressive':
            link = self.browser.find_element(*ElementsPageLocators.RADIO_BUTTON_SUB_TUB_IMPRESSIVE_BTN)
            link.click()

    def should_be_needed_message(self, button):
        LOGGER.info('should_be_needed_message')
        message = self.browser.find_element(*ElementsPageLocators.RADIO_BUTTON_SUB_TUB_MESSAGE).text
        LOGGER.info(f'Actual message: {message}')
        expected_message = RADIO_BUTTON_SUCCESSFUL_MESSAGE + button
        LOGGER.info(f'Expected message: {expected_message}')
        assert message == expected_message, \
            'The message on radio button sub-tub is different from expected. ' \
            f'Expected: {expected_message}, actual: {message}'
