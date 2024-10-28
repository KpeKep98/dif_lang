import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def test_language(browser):
    browser.get('https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/')
    try:
        find_button = browser.find_element(By.XPATH, '//*[@id="add_to_basket_form"]/but')
        assert find_button, 'Элемент не найден'
    except NoSuchElementException:
        assert False, 'Элемент не найден 2'
