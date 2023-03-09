import inspect
import logging

import pytest

from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass():

    def synchronization(self):
        wait = WebDriverWait(self.driver, 30)
        return wait

    def getLogger(self):

        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler('.//logs//automation.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)

        # Accept filehandler object
        logger.addHandler(fileHandler)

        # printing the output
        # heirarchy
        logger.setLevel(logging.DEBUG)
        return logger