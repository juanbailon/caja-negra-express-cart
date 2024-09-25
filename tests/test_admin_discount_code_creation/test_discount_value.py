import random
from .set_up import DiscountCodeCreationTestSetup
import browser_elements
import utils


class TestDiscountPercentValue(DiscountCodeCreationTestSetup):

    def setUp(self):
        return super().setUp(discount_type = "percent")
    
    def test_discount_percent_value_equal_to_zero(self):    
        self.set_discount_value(value= 0)

        self.click_add_discount_button()

        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)

    
    def test_discount_percent_value_less_than_zero(self):
        self.set_discount_value(value= -1)
        self.click_add_discount_button()

        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)


    def test_discount_percent_value_greater_than_100(self):        
        self.set_discount_value(value= 101)
        self.click_add_discount_button()

        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)


    def test_discount_percent_value_equal_to_100(self):        
        self.set_discount_value(value= 100)
        self.click_add_discount_button()

        is_visible = browser_elements.notify_message_alert_success_is_visible(driver= self.driver)
        self.assertTrue(is_visible)


    def test_discount_percent_value_equal_to_1(self):        
        self.set_discount_value(value= 1)
        self.click_add_discount_button()

        is_visible = browser_elements.notify_message_alert_success_is_visible(driver= self.driver)
        self.assertTrue(is_visible)


    def test_discount_percent_value_equal_to_99(self):        
        self.set_discount_value(value= 99)
        self.click_add_discount_button()

        is_visible = browser_elements.notify_message_alert_success_is_visible(driver= self.driver)
        self.assertTrue(is_visible)


    def test_discount_percent_value_between_0_and_100(self):
        value = random.randint(1, 99)        
        self.set_discount_value(value= value)
        self.click_add_discount_button()

        is_visible = browser_elements.notify_message_alert_success_is_visible(driver= self.driver)
        self.assertTrue(is_visible)


    def test_discount_percent_value_with_float(self):
        value = random.uniform(1, 99)
        value = round(value, 2) 
        self.set_discount_value(value= value)
        self.click_add_discount_button()

        input_element = browser_elements.get_discount_value_input(driver= self.driver)
        self.assert_focus_or_border_color(element= input_element)


    def test_discount_percent_value_empty(self):
        value_input = browser_elements.get_discount_value_input(self.driver)
        value_input.clear()
        self.click_add_discount_button()

        input_element = browser_elements.get_discount_value_input(driver= self.driver)
        self.assert_focus_or_border_color(element= input_element)

    
    def test_discount_percent_value_wiht_none_numeric_chars_only(self):
        value = utils.generate_random_string(size= 8)  
        self.set_discount_value(value= value)
        self.click_add_discount_button()

        input_element = browser_elements.get_discount_value_input(driver= self.driver)
        self.assert_focus_or_border_color(element= input_element)



class TestDiscountAmountValue(DiscountCodeCreationTestSetup):

    def setUp(self):
        return super().setUp(discount_type = "amount")

    def test_discount_amount_value_equal_to_zero(self):
        self.set_discount_value(value= 0)
        self.click_add_discount_button()

        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)

    def test_discount_amount_value_less_that_zero(self):        
        self.set_discount_value(value= -1)
        self.click_add_discount_button()

        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)

    def test_discount_amount_value_greater_to_zero(self):
        value = random.randint(1, 10000)        
        self.set_discount_value(value= value)
        self.click_add_discount_button()

        is_visible = browser_elements.notify_message_alert_success_is_visible(driver= self.driver)
        self.assertTrue(is_visible)

    def test_discount_amount_value_equal_to_1(self):
        value = 1      
        self.set_discount_value(value= value)
        self.click_add_discount_button()

        is_visible = browser_elements.notify_message_alert_success_is_visible(driver= self.driver)
        self.assertTrue(is_visible)

    def test_discount_amount_value_with_float(self):
        value = random.uniform(5, 1000)
        value = round(value, 2)        
        self.set_discount_value(value= value)
        self.click_add_discount_button()

        is_visible = browser_elements.notify_message_alert_success_is_visible(driver= self.driver)
        self.assertTrue(is_visible)

    
    def test_discount_amount_value_empty(self):
        value_input = browser_elements.get_discount_value_input(self.driver)
        value_input.clear()
        self.click_add_discount_button()

        input_element = browser_elements.get_discount_value_input(driver= self.driver)
        self.assert_focus_or_border_color(element= input_element)


    def test_discount_amount_value_wiht_none_numeric_chars_only(self):
        value = utils.generate_random_string(size= 8)  
        self.set_discount_value(value= value)
        self.click_add_discount_button()

        input_element = browser_elements.get_discount_value_input(driver= self.driver)
        self.assert_focus_or_border_color(element= input_element)