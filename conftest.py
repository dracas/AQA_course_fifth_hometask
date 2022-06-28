import datetime
import pytest
import logging
from selenium import webdriver

LOGGER = logging.getLogger()


@pytest.fixture(scope="function")
def browser():
    LOGGER.info("start browser for test..")
    browser = webdriver.Chrome()
    yield browser
    now = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    browser.save_screenshot(f'Screenshots/{now}.png')
    LOGGER.info("quit browser..")
    browser.quit()
