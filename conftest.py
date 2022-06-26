import datetime
import pytest
import logging
from selenium import webdriver
from Screenshot import Screenshot_Clipping

LOGGER = logging.getLogger()


@pytest.fixture(scope="function")
def browser():
    LOGGER.info("start browser for test..")
    browser = webdriver.Chrome()
    yield browser
    now = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    ob = Screenshot_Clipping.Screenshot()
    ob.full_Screenshot(browser, save_path='Screenshots/', image_name=f'{now}.png')
    LOGGER.info("quit browser..")
    browser.quit()