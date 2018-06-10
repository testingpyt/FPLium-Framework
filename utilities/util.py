import time
import traceback
import utilities.custom_logger as cl
import logging


class Util(object):

    log = cl.customLogger(logging.INFO)

    def sleep(self, sec, info=""):
        """
        Put the program to wait for the specified amount of time
        """
        if info is not None:
            self.log.info("Wait :: '" + str(sec) + "' seconds for " + info)
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()

    def verify_text_contains(self, actual_text, expected_text):
        """
        Verify actual text contains expected text string

        Parameters:
            actual_text: Expected Text
            expected_text: Actual Text
        """
        if expected_text.lower() in actual_text.lower():
            self.log.info("### TEXT VERIFICATION SUCCESS !!!")
            return True
        else:
            self.log.info("### TEXT VERIFICATION FAILED !!!")
            return False
