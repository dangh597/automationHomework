import unittest
from selenium import webdriver
import logging
import warnings
from selenium.webdriver.firefox.options import Options


class WebDriverSetup(unittest.TestCase):
    def setUp(self):
        logging.info("Setting up browser")
        warnings.simplefilter('ignore', ResourceWarning)
        options = Options()
        options.headless = True
        self.driver = webdriver.Firefox(options=options)

    def tearDown(self):
        if self.driver is not None:
            logging.info("Closing browser")
            self.driver.close()
            self.driver.quit()
