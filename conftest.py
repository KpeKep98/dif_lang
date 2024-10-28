import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def browser():
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    yield browser
    browser.quit()

#@pytest.mark.parametrize('language'):
