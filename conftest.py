import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser(request):
    service = Service(ChromeDriverManager().install())
    options = Options()

    language = request.config.getoption("--language")
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(service=service, options=options)
    yield browser
    browser.quit()


def pytest_addoption(parser):
    parser.addoption("--language", default="en")
