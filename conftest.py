import pytest
from selenium import webdriver
import logging
LOGGER = logging.getLogger()


@pytest.fixture(scope="function")
def browser():
    LOGGER.info("start browser for test..")
    browser = webdriver.Chrome()
    yield browser
    LOGGER.info("quit browser..")
    browser.quit()
