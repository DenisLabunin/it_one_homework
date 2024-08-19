import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(autouse=True)
def browser(request):
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
