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
        cls.driver.get(settings.ADMIN_CREATE_DISCOUNT_CODE_URL)

    @classmethod
    def tearDownClass(cls):
        # Cleanup code that runs once after all tests
        cls.driver.quit()  # Close the browser driver


class DiscountCodeCreationTestSetup(BaseAdminPanelTestSetup):
    def setUp(self, discount_type: str = None):
        # Setup code
        self.driver.get(settings.ADMIN_CREATE_DISCOUNT_CODE_URL)
        self.discount_code = utils.generate_random_string(size= 8)
        self.valid_discount_types = ['amount', 'percent']
        self.discount_value = random.randint(1, 100)

        self.start_time = datetime.now() + timedelta(days= 2)
        self.end_time = datetime.now() + timedelta(days= 5)
        self.start_time_str = utils.parse_datetime_to_european_format(self.start_time)
        self.end_time_str = utils.parse_datetime_to_european_format(self.end_time)

        discount_code_input = browser_elements.get_discount_code_input(driver= self.driver)
        discount_code_input.clear()
        discount_code_input.send_keys(self.discount_code)
        
        if not discount_type:
            self.discount_type = random.choice(self.valid_discount_types)
        else:
            self.discount_type = discount_type

        self.set_discount_type_and_value(discount_type= self.discount_type,
                                         value= self.discount_value)
        
        discount_start_input = browser_elements.get_discount_start_input(driver= self.driver)
        browser_scripts.set_element_value_attr(driver= self.driver,
                                               element= discount_start_input,
                                               value= self.start_time_str
                                               )
        
        discoutn_end_input = browser_elements.get_discount_end_input(driver= self.driver)
        browser_scripts.set_element_value_attr(driver= self.driver,
                                               element= discoutn_end_input,
                                               value= self.end_time_str
                                               )


    def click_add_discount_button(self):
        button = browser_elements.get_add_discount_button(driver= self.driver)
        button.click()

    def set_discount_value(self, value: int|float):
        value_input = browser_elements.get_discount_value_input(driver= self.driver, element_timeout= 3)
        value_input.clear()
        value_input.send_keys(value)

    def set_discount_type_and_value(self, discount_type:str, value: int|float):
        browser_automation.select_discount_type(driver= self.driver, discount_type= discount_type)
        self.set_discount_value(value= value)

    def set_discount_code_text(self, code: str):
        code_input = browser_elements.get_discount_code_input(driver= self.driver)
        code_input.clear()
        code_input.send_keys(code)

    
    def set_discount_code_text_using_javascript(self, code: str):
        code_input = browser_elements.get_discount_code_input(driver= self.driver)
        browser_scripts.set_element_value_attr(driver= self.driver,
                                               element= code_input,
                                               value= code
                                            )
        

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
            self.assertTrue(is_color_match)


    def set_start_date_value(self, start_time: datetime):
        start_date_element = browser_elements.get_discount_start_input(driver= self.driver)
        start_time_str = utils.parse_datetime_to_european_format(start_time)

        browser_scripts.set_element_value_attr(driver= self.driver,
                                               element= start_date_element,
                                               value= start_time_str
                                            )
        
    def set_start_date_value_string(self, start_time_str: str):
        start_date_element = browser_elements.get_discount_start_input(driver= self.driver)

        browser_scripts.set_element_value_attr(driver= self.driver,
                                               element= start_date_element,
                                               value= start_time_str
                                            )
        
    def set_end_date_value(self, end_time: datetime):
        end_date_element = browser_elements.get_discount_end_input(driver= self.driver)
        end_time_str = utils.parse_datetime_to_european_format(end_time)

        browser_scripts.set_element_value_attr(driver= self.driver,
                                               element= end_date_element,
                                               value= end_time_str
                                            )       
        
    def set_end_date_value_string(self, end_time_str: str):
        end_date_element = browser_elements.get_discount_end_input(driver= self.driver)

        browser_scripts.set_element_value_attr(driver= self.driver,
                                               element= end_date_element,
                                               value= end_time_str
                                            )  

