import unittest
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from typing import Any
import browser_automation
import browser_elements
import browser_scripts
import settings
import utils
import time

class BaseTestSetup(unittest.TestCase):
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

    def setUp(self) -> None:
        super().setUp()
        self.valid_smtp_vars = {
            "host": "smtp.example.com",
            "port": 587,
            "username": "hi@markmoffat.com",
            "password": "my_secret_123#@",
            "secure": True
        }

    def run_test_SMTP_varibles_updated_seccessfully(self):
        is_visible = browser_elements.notify_message_alert_success_is_visible(driver= self.driver, element_timeout=3)
        self.assertTrue(is_visible, "Success message was NOT display")

    def run_test_SMTP_varibles_update_error(self):
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver, element_timeout=3)
        self.assertTrue(is_visible, "Error message was NOT display")


    
    def set_valid_smtp_values(self):
        host =browser_elements.get_SMTP_host_input(driver= self.driver)
        host.clear()
        host.send_keys(self.valid_smtp_vars['host'])

        port =browser_elements.get_SMTP_port_input(driver= self.driver)
        port.clear()
        port.send_keys(self.valid_smtp_vars['port'])

        username =browser_elements.get_SMTP_username_input(driver= self.driver)
        username.clear()
        username.send_keys(self.valid_smtp_vars['username'])

        password =browser_elements.get_SMTP_password_input(driver= self.driver)
        password.clear()
        password.send_keys(self.valid_smtp_vars['password'])

        secure_checkbox =browser_elements.get_SMTP_email_secure_checkbox(driver= self.driver)
        if not secure_checkbox.is_selected() and self.valid_smtp_vars['secure']:
            secure_checkbox.click()


    def click_update_btn(self):
        update = browser_elements.get_update_btn_admin_page(driver= self.driver)
        update.click()


    def assert_focus_or_border_color(self, element: WebElement,
                                     expected_border_rgb_color: tuple = (204, 65, 53), # 'rgb(204, 65, 53)
                                     assert_msg: Any = None):
        active_element = self.driver.switch_to.active_element
        if active_element == element:
            # If the input element is focused, the test passes
            pass
        else:
            # If the input element is not focused, check the border color
            border_color = element.value_of_css_property("border-color")  #returns a str like this 'rgb(100, 155, 10)'
            msg = assert_msg
            if not assert_msg:
                msg = "The border color does not match the expected highlight color."

            rgb_border_color = utils.extract_rgb_values(border_color)
            is_color_match = utils.is_color_within_margin(color= rgb_border_color,
                                                          target_color= expected_border_rgb_color,
                                                          margin= 5
                                                          )
            self.assertTrue(is_color_match, msg)