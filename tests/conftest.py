import pytest
from base.webdriver_factory import WebDriverFactory


@pytest.yield_fixture()
def setup_before():
    print("Prepare something before test")
    yield
    print("Destroy something after test")


@pytest.yield_fixture(scope="class")
def onetime_setup(request, browser, url, username, password):
    print("Creating browser driver instance")
    wdf = WebDriverFactory(browser)
    if url is None:
        url = "http://fantasy.premierleague.com/"
    driver = wdf.get_web_driver_instance(url)
    if username is None:
        username = "testingpy@outlook.com"
    if password is None:
        password = "testingPython"
    if request.cls is not None:
        request.cls.driver = driver
        request.cls.username = username
        request.cls.password = password
    yield driver, url, username, password
    driver.quit()
    print("Browser driver instance is destroyed")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--os")
    parser.addoption("--url", help="The url we are going to work with")
    parser.addoption("--username")
    parser.addoption("--password")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def os(request):
    return request.config.getoption("--os")


@pytest.fixture(scope="session")
def username(request):
    return request.config.getoption("--username")


@pytest.fixture(scope="session")
def password(request):
    return request.config.getoption("--password")


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")

