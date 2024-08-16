import time

import pytest
from selenium import webdriver
from locators import *


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.get(base_url)

    browser.find_element('xpath', user_name).send_keys(value_user_name)
    browser.find_element('xpath', password).send_keys(value_password)
    browser.find_element('xpath', login_button).click()
    yield browser

    browser.quit()

def test_autorization(browser):
    time.sleep(2)
    assert browser.current_url == url_after_login, 'url не соответствует'

