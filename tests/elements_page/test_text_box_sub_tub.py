from pytest_bdd import scenario, given, when, then

from ...test_data.constants import MAIN_PAGE_LINK
from ...pages.elements_page.text_box_sub_tub import TextBoxSubTub

import logging
LOGGER = logging.getLogger()


@scenario('elements_page/text_box_sub_tub.feature', "There is text-box form")
def test_text_box_form():
    pass


@given("I'm on Elements page")
def open_elements_page(browser):
    LOGGER.info("open_elements_page")
    page = TextBoxSubTub(browser, MAIN_PAGE_LINK)
    page.open()
    page.go_to_elements_page()


@when("I open text-box sub-tub")
def go_to_text_box_sub_tub(browser):
    LOGGER.info("go_to_text_box_sub_tub")
    current_page_url = browser.current_url
    TextBoxSubTub(browser, current_page_url).go_to_text_box_sub_tub()


@then("I see the text-box form")
def check_text_box_form(browser):
    LOGGER.info("check_text_box_form")
    current_page_url = browser.current_url
    TextBoxSubTub(browser, current_page_url).should_be_text_box_form_on_text_box_sub_tub()


@then("I see Submit button")
def check_submit_button(browser):
    LOGGER.info("check_submit_button")
    current_page_url = browser.current_url
    TextBoxSubTub(browser, current_page_url).should_be_submit_button_on_text_box_sub_tub()

