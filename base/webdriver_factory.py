import os
from selenium import webdriver


class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser

    def get_web_driver_instance(self, url):
        base_url = url
        if self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            chrome_driver_location = "/usr/local/bin/chromedriver"
            os.environ["webdriver.chrome.driver"] = chrome_driver_location
            driver = webdriver.Chrome(chrome_driver_location)
        else:
            driver = webdriver.Firefox()
        driver.implicitly_wait(3)
        driver.get(base_url)
        return driver

