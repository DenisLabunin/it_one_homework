from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 5)

    def open(self, url):
        self.browser.get(url)
