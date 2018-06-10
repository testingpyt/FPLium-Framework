from base.basepage import BasePage
import utilities.custom_logger as cl
import logging


class LoginPage(BasePage):

    # Overriding to know where the log messages are coming from
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _username_field = "ismjs-username"
    _password_field = "ismjs-password"
    _login_button = "//button[contains(@class, 'ismjs-submit btn btn-primary ism-button ism-button--full')]"

    def click_login_button(self):
        self.element_click(self._login_button, locator_type="xpath")

    def enter_username(self, username):
        self.sending_keys(username, self._username_field)

    def enter_password(self, password):
        self.sending_keys(password, self._password_field)

    def login(self, username="", password=""):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def verify_login_successful(self):
        return self.is_element_present("//h2[contains(@class, 'subHeader ism-sub-header')]", locator_type="xpath")

    def verify_login_failed(self):
        return self.is_element_present("//p[contains(text(),'Incorrect email or password')]", locator_type="xpath")

    def verify_login_title(self):
        return self.verify_page_title("Fantasy Premier League, Official Fantasy Football Game of the Premier League")
