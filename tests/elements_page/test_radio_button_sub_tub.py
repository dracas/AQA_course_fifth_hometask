import logging
from pytest_bdd import scenario, given, when, then, parsers
from ...test_data.constants import MAIN_PAGE_LINK
from ...pages.elements_page.radio_button_sub_tub import RadioButtonSubTub
LOGGER = logging.getLogger()


@scenario('elements_page/radio_button_sub_tub.feature', "Verification of messages")
def test_check_message():
    LOGGER.info(test_check_message)
    pass


@given("I'm on Elements page")
def open_elements_page(browser):
    LOGGER.info("open_elements_page")
    page = RadioButtonSubTub(browser, MAIN_PAGE_LINK)
    page.open()
    page.go_to_elements_page()


@given("I'm on Radio Button sub-tab")
def open_radio_button_sub_tub(browser):
    LOGGER.info("open_radio_button_sub_tub")
    current_page_url = browser.current_url
    RadioButtonSubTub(browser, current_page_url).go_to_radio_button_sub_tub()


@when(parsers.parse('I select {button}'))
def click_on_indicated_button(browser, button):
    LOGGER.info('click_on_indicated_button')
    current_page_url = browser.current_url
    RadioButtonSubTub(browser, current_page_url).click_on_button(button)


@then(parsers.parse("I see message 'You have selected {button}'"))
def compare_messages(browser, button):
    LOGGER.info('compare_messages')
    current_page_url = browser.current_url
    RadioButtonSubTub(browser, current_page_url).should_be_needed_message(button)
