

import utilities.custom_logger as cl
import logging
from base.selenium_driver import SeleniumDriver


class StatusManager(SeleniumDriver):

    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        super(StatusManager, self).__init__(driver)
        self.result_list = []

    def set_result(self, result, result_message):
        try:
            if result is not None:
                if result:
                    self.result_list.append("PASS")
                    self.log.info("### VERIFICATION SUCCESSFUL :: " + result_message)
                else:
                    self.result_list.append("FAIL")
                    self.log.error("### VERIFICATION FAILED :: " + result_message)
                    self.take_screenshot(result_message)
            else:
                self.result_list.append("FAIL")
                self.log.error("### VERIFICATION FAILED :: " + result_message)
                self.take_screenshot(result_message)
        except:
            self.result_list.append("FAIL")
            self.log.error("### Exception Occurred !!!")
            self.take_screenshot(result_message)

    def mark(self, result, result_message):
        self.set_result(result, result_message)

    def mark_final(self, test_name, result, result_message):
        self.set_result(result, result_message)

        if "FAIL" in self.result_list:
            self.log.error(test_name + " ### TEST FAILED")
            self.result_list.clear()
            assert True == False
        else:
            self.log.info(test_name + " ### TEST SUCCESSFUL")
            self.result_list.clear()
            assert True == True