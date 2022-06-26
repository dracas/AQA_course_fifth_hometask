import logging
from pytest_bdd import scenario, given, when, then
from ...test_data.constants import MAIN_PAGE_LINK
from ...pages.elements_page.buttons_sub_tub import ButtonsSubTub
LOGGER = logging.getLogger()


@scenario('elements_page/buttons_sub_tub.feature', "Click on Click Me button")
def test_click_button():
    LOGGER.info("test_click_button")
    pass


@given("I'm on Elements page")
def open_elements_page(browser):
    LOGGER.info("open_elements_page")
    page = ButtonsSubTub(browser, MAIN_PAGE_LINK)
    page.open()
    page.go_to_elements_page()


@given("I'm on Buttons sub-tab")
def open_buttons_sub_tub(browser):
    LOGGER.info("open_buttons_sub_tub")
    current_page_url = browser.current_url
    ButtonsSubTub(browser, current_page_url).go_to_buttons_sub_tub()


@when("I click on Click Me button")
def click_on_click_me_button(browser):
    LOGGER.info("click_on_click_me_button")
    current_page_url = browser.current_url
    ButtonsSubTub(browser, current_page_url).click_on_click_me_button()


@then("I see 'You have done a dynamic click' message")
def check_message_after_click_to_click_me_button(browser):
    LOGGER.info("check_message_after_click_to_click_me_button")
    current_page_url = browser.current_url
    ButtonsSubTub(browser, current_page_url).should_be_needed_message_after_click_to_click_me_button()


@scenario('elements_page/buttons_sub_tub.feature', "Click on Double Click Me button")
def test_double_click_button():
    LOGGER.info("test_double_click_button")
    pass


@when("I do double-click on Double Click Me button")
def click_on_double_click_me_button(browser):
    LOGGER.info("click_on_double_click_me_button")
    current_page_url = browser.current_url
    ButtonsSubTub(browser, current_page_url).double_click_on_button()


@then("I see 'You have done a double click' message")
def check_message_after_click_to_double_click_me_button(browser):
    LOGGER.info("check_message_after_click_to_double_click_me_button")
    current_page_url = browser.current_url
    ButtonsSubTub(browser, current_page_url).should_be_needed_message_after_click_to_double_click_me_button()
