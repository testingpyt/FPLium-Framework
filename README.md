# FPLium

A small automation framework to run automatic testing of Fantasy Premier League

## Getting Started

### Prerequisites
Download

* [chromedriver](https://github.com/mozilla/geckodriver/releases)
* [geckodriver](http://chromedriver.chromium.org/downloads)

### Installing

Move chromedriver and geckodriver to a folder included in your PATH

To use chromedriver you will need to edit the code of **webdriver_factory.py**

You will need to change **chrome_driver_location** to your chromedriver location

For example in Linux you can place them in /usr/local/bin so it will be /usr/local/bin/chromedriver
```
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


```

Also you will need to add some python modules that are used by the framework 

```
pip install pytest pytest-ordering selenium
```

## Running the tests
To run the tests open the terminal in the root dir of the project

Before running you will need to add the project folders and files to your PYTHONPATH

For example in Linux 
```
export PYTHONPATH=$PYTHONPATH:. 
```
Then to run tests

```
py.test login_tests.py
```

To run a test with custom parameters

```
py.test login_tests.py --browser chrome --username testingpyt@outlook.com --password testingPython --url https://fantasy.premierleague.com/
```

### Framework Structure
    .
    ├── base                        # Base files
    │   ├── basepage.py             # Handles base page functionality 
    │   ├── selenium_driver.py      # Custom wrapper for WebDriver for validation and logging of WebDriver methods
    │   └── webdriver_factory.py    # Handles the creation of the appropriate driver instance
    |
    ├── pages                       # Page Object files
    |   └── home                    # Home Objects
    |       └── login_page.py       # Login page object
    |
    ├── screenshots                 # Holds screenshots 
    |
    ├── tests                       # Tests
    |   ├──  conftest.py            # Handles the configuration of test execution
    |   ├── home
    |       └── login_tests.py      # Tests login scenarios
    |
    ├── utilities                   # Utilities 
    |   ├──  custom_logger.py       # Handles logging
    |   ├──  status_manager.py      # Handles test logging and screenshot capturing
    │   └──  webdriver_factory.py   # Helps with handling general functions
    |
    ├── automation.log              # Log file
    .
## TODO
* Improve logging 
* Add more utilities 
* Add more example tests


