import browser_automation
import browser_elements
from set_up import BaseTestSetup
import settings
import time


class TestUpdateSMTPVariables(BaseTestSetup):
    
    def test_valid_smtp_values(self):
        self.set_valid_smtp_values()
        self.click_update_btn()
        self.run_test_SMTP_varibles_updated_seccessfully()


    def test_invalid_host_TLD_domain(self):
        self.set_valid_smtp_values()
        host = browser_elements.get_SMTP_host_input(driver= self.driver)
        host.clear()
        host.send_keys("smtp.my-company")
        self.click_update_btn()
        self.run_test_SMTP_varibles_update_error()

    def test_invalid_host_with_special_chars_domain(self):
        self.set_valid_smtp_values()
        host = browser_elements.get_SMTP_host_input(driver= self.driver)
        host.clear()
        host.send_keys("smtp@!example.com")
        self.click_update_btn()
        self.run_test_SMTP_varibles_update_error()


    def test_port_out_of_range(self):
        self.set_valid_smtp_values()
        port = browser_elements.get_SMTP_port_input(driver= self.driver)
        port.clear()
        port.send_keys(65536)
        self.click_update_btn()
        self.run_test_SMTP_varibles_update_error()

    def test_port_equal_to_zero(self):
        self.set_valid_smtp_values()
        port = browser_elements.get_SMTP_port_input(driver= self.driver)
        port.clear()
        port.send_keys(0)
        self.click_update_btn()
        self.run_test_SMTP_varibles_update_error()

    def test_port_negative_number(self):
        self.set_valid_smtp_values()
        port = browser_elements.get_SMTP_port_input(driver= self.driver)
        port.clear()
        port.send_keys("-17")
        self.click_update_btn()
        self.run_test_SMTP_varibles_update_error()

    def test_port_is_non_numeric_value(self):
        self.set_valid_smtp_values()
        port = browser_elements.get_SMTP_port_input(driver= self.driver)
        port.clear()
        port.send_keys("hola")
        self.click_update_btn()
        self.run_test_SMTP_varibles_update_error()


    def test_password_is_empty(self):
        self.set_valid_smtp_values()
        password = browser_elements.get_SMTP_password_input(driver= self.driver)
        password.clear()
        self.click_update_btn()
        self.assert_focus_or_border_color(element= password)

    def test_username_is_empty(self):
        self.set_valid_smtp_values()
        username = browser_elements.get_SMTP_username_input(driver= self.driver)
        username.clear()
        self.click_update_btn()
        self.assert_focus_or_border_color(element= username)

    
    def test_inactive_secure_email(self):
        self.set_valid_smtp_values()
        secure_checkbox = browser_elements.get_SMTP_email_secure_checkbox(driver= self.driver)
        
        if secure_checkbox.is_selected():
            secure_checkbox.click()

        self.click_update_btn()
        self.run_test_SMTP_varibles_updated_seccessfully()

        
