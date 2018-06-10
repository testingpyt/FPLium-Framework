from pages.home.login_page import LoginPage
from utilities.status_manager import StatusManager
import unittest
import pytest


@pytest.mark.usefixtures("onetime_setup", "setup_before")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, onetime_setup):
        self.lp = LoginPage(self.driver)
        self.ts = StatusManager(self.driver)

    # Just to show that we can control the order of pytest execution
    @pytest.mark.run(order=4)
    def test_valid_login(self):
        result1 = self.lp.verify_login_title()
        self.ts.mark(result1, "Title Verification")
        self.lp.login(self.username, self.password)
        result2 = self.lp.verify_login_successful()
        self.ts.mark_final("test_valid_login", result2, "Successful login")

    @pytest.mark.run(order=1)
    def test_invalid_login_password(self):
        result1 = self.lp.verify_login_title()
        self.ts.mark(result1, "Title Verification")
        self.lp.login(self.username, "badpassword")
        result2 = self.lp.verify_login_failed()
        self.ts.mark_final("test_invalid_login_password", result2, "Fail to login with wrong password")

    @pytest.mark.run(order=2)
    def test_empty_login_password(self):
        result1 = self.lp.verify_login_title()
        self.ts.mark(result1, "Title Verification")
        self.lp.login(self.username, "")
        result2 = self.lp.verify_login_failed()
        self.ts.mark_final("test_empty_login_password", result2, "Fail to login without password")

    @pytest.mark.run(order=3)
    def test_empty_login_credentials(self):
        result1 = self.lp.verify_login_title()
        self.ts.mark(result1, "Title Verification")
        self.lp.login("", "")
        result2 = self.lp.verify_login_failed()
        self.ts.mark_final("test_empty_login_credentials", result2, "Fail to login without username and password")

