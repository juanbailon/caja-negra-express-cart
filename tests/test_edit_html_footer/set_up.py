import unittest
import random
import string
from datetime import datetime, timedelta
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from typing import Any
import browser_automation
import browser_elements
import browser_scripts
import settings
import utils
import time

class BaseAdminPanelTestSetup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Setup code that runs once for all tests
        cls.admin_email = settings.ADMIN_EMAIL
        cls.admin_password = settings.ADMIN_PASSWORD
        cls.driver = browser_automation.create_chrome_web_driver_conection(headless= settings.IS_HEADLESS)
        cls.driver.get(settings.ADMIN_LOGIN_URL)
        browser_automation.admin_login(cls.driver, cls.admin_email, cls.admin_password)
        browser_automation.wait(2)
        cls.driver.get(settings.ADMIN_SETTINGS_URL)

    @classmethod
    def tearDownClass(cls):
        # Cleanup code that runs once after all tests
        cls.driver.quit()  # Close the browser driver


    def run_test_html_footer_updated_seccessfully(self):
        is_visible = browser_elements.notify_message_alert_success_is_visible(driver= self.driver, element_timeout=3)
        self.assertTrue(is_visible, "Success message was NOT display")

    def run_test_html_footer_update_error(self):
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver, element_timeout=3)
        self.assertTrue(is_visible, "Error message was NOT display")
