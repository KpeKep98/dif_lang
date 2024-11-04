import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def test_language(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    try:
        find_button = browser.find_element(By.XPATH, '//*[@id="add_to_basket_form"]/button')
        # time.sleep()
        assert find_button
    except NoSuchElementException:
        assert False, 'Элемент не найден!'
