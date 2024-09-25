import random
import string
from datetime import datetime, timedelta
from .set_up import DiscountCodeCreationTestSetup
import browser_elements
import utils


class TestDiscountCodeStartDate(DiscountCodeCreationTestSetup):

        
    def run_website_start_time_equal_to_test(self, start_time: datetime|str):
        """ Auxiliar function, this method is NOT consider a test by the unittest lib """
        if isinstance(start_time, datetime):
            start_time_str = utils.parse_datetime_to_european_format(start_time)
        else:
            start_time_str = start_time

        website_start_time = browser_elements.get_discount_start_input(self.driver).get_attribute('value')
        # website_start_time = website_start_time.replace('"', '')

        self.assertEqual(website_start_time, start_time_str)

    
    def run_website_start_time_NOT_equal_to_test(self, start_time: datetime):
        """ Auxiliar function, this method is NOT consider a test by the unittest lib """
        website_start_time = browser_elements.get_discount_start_input(self.driver).get_attribute('value')
        start_time_str = utils.parse_datetime_to_european_format(start_time)
        self.assertNotEqual(website_start_time, start_time_str)


    def test_valid_start_date(self):
        start_time = datetime.now() + timedelta(days= 1, hours=1)
        self.set_start_date_value(start_time= start_time)
        self.run_website_start_time_equal_to_test(start_time= start_time)
        self.click_add_discount_button()

        is_visible = browser_elements.notify_message_alert_success_is_visible(driver= self.driver)
        self.assertTrue(is_visible)

    def test_start_date_equal_to_now(self):
        start_time = datetime.now()
        self.set_start_date_value(start_time= start_time)
        self.run_website_start_time_equal_to_test(start_time= start_time)
        
        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_success_is_visible(driver= self.driver)
        self.assertTrue(is_visible)


    def test_start_date_is_a_past_date(self):
        start_time = datetime.now() - timedelta(hours= 10)
        self.set_start_date_value(start_time= start_time)
        self.run_website_start_time_equal_to_test(start_time= start_time)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)

    
    def test_start_date_is_greater_than_now_for_lees_than_a_day(self):
        start_time = datetime.now() + timedelta(hours= 15)
        self.set_start_date_value(start_time= start_time)
        self.run_website_start_time_equal_to_test(start_time= start_time)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_success_is_visible(driver= self.driver)
        self.assertTrue(is_visible)

    def test_start_date_is_greater_than_now_for_exactly_a_day(self):
        start_time = datetime.now() + timedelta(days= 1)
        self.set_start_date_value(start_time= start_time)
        self.run_website_start_time_equal_to_test(start_time= start_time)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_success_is_visible(driver= self.driver)
        self.assertTrue(is_visible)


    def test_start_date_is_greater_than_end_date(self):
        start_time = self.end_time + timedelta(hours= 1)
        self.set_start_date_value(start_time= start_time)
        self.run_website_start_time_equal_to_test(start_time= start_time)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)


    def test_start_date_with_trailing_whitespace_chars(self):
        trailing_size = random.randint(3, 8)
        whitespaces = utils.generate_random_string(size= trailing_size, char_set= string.whitespace)
        start_time_str = self.start_time_str + whitespaces
        self.set_start_date_value_string(start_time_str= start_time_str)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)


    def test_start_date_with_leading_whitespace_chars(self):
        leading_size = random.randint(3, 8)
        whitespaces = utils.generate_random_string(size= leading_size, char_set= string.whitespace)
        start_time_str = whitespaces + self.start_time_str
        self.set_start_date_value_string(start_time_str= start_time_str)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)


    def test_start_date_with_leading_and_trailing_whitespace_chars(self):
        size = random.randint(3, 8)
        leading = utils.generate_random_string(size= size, char_set= string.whitespace)
        trailing = utils.generate_random_string(size= size, char_set= string.whitespace)
        start_time_str = leading + self.start_time_str + trailing
        self.set_start_date_value_string(start_time_str= start_time_str)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)
        
        
    def test_start_date_is_invalid_date(self):
        start_time_str = "31/11/2100 13:00"
        end_time_str = "10/12/2100 14:30"
        self.set_start_date_value_string(start_time_str= start_time_str)
        self.set_end_date_value_string(end_time_str= end_time_str)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)


    def test_start_date_with_invalid_hour(self):
        start_time_str = "31/11/2100 32:20"
        end_time_str = "10/12/2100 14:30"
        self.set_start_date_value_string(start_time_str= start_time_str)
        self.set_end_date_value_string(end_time_str= end_time_str)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)

    def test_start_date_with_invalid_minute(self):
        start_time_str = "31/11/2100 2:89"
        end_time_str = "10/12/2100 14:30"
        self.set_start_date_value_string(start_time_str= start_time_str)
        self.set_end_date_value_string(end_time_str= end_time_str)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)

    
    def test_start_date_without_an_specific_hour(self):
        date_part, time_part = self.start_time_str.split(' ')
        start_time_str = date_part
        self.set_start_date_value_string(start_time_str= start_time_str)
     
        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)

    
    def test_start_date_with_chars_between_the_date_and_hour(self):
        chars = utils.generate_random_string(size=8)
        start_time_str = utils.insert_str_between_the_date_and_hour(date_str= self.start_time_str, insert_str= chars)
        self.set_start_date_value_string(start_time_str= start_time_str)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)

    
    def test_start_date_with_letters_only(self):
        size = random.randint(5, 20)
        start_time_str = utils.generate_random_string(size= size, char_set= string.ascii_letters) 
        self.set_start_date_value_string(start_time_str= start_time_str)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)


    def test_start_date_with_numbers_only(self):
        size = random.randint(5, 20)
        start_time_str = utils.generate_random_string(size= size, char_set=string.digits) 
        self.set_start_date_value_string(start_time_str= start_time_str)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)


    def test_start_date_with_whitespace_chars_only(self):
        size = random.randint(5, 20)
        start_time_str = utils.generate_random_string(size= size, char_set=string.whitespace) 
        self.set_start_date_value_string(start_time_str= start_time_str)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)


    def test_start_date_with_punctiation_chars_only(self):
        size = random.randint(5, 20)
        start_time_str = utils.generate_random_string(size= size, char_set=string.punctuation) 
        self.set_start_date_value_string(start_time_str= start_time_str)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)


    def test_start_date_with_trailing_chars(self):
        trailing_size = random.randint(5, 15)
        trailing_chars = utils.generate_random_string(size= trailing_size, char_set= string.printable)
        start_time_str = self.start_time_str + trailing_chars
        self.set_start_date_value_string(start_time_str= start_time_str)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)


    def test_start_date_with_leading_chars(self):
        leadingsize = random.randint(5, 15)
        leading_chars = utils.generate_random_string(size= leadingsize, char_set= string.printable)
        start_time_str = leading_chars + self.start_time_str
        self.set_start_date_value_string(start_time_str= start_time_str)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)


    def test_start_date_with_leading_and_trailing_chars(self):
        size = random.randint(5, 15)
        leading_chars = utils.generate_random_string(size= size, char_set= string.printable)
        trailing_chars = utils.generate_random_string(size= size, char_set= string.printable)
        start_time_str = leading_chars + self.start_time_str + trailing_chars
        self.set_start_date_value_string(start_time_str= start_time_str)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)


    def test_start_date_with_chars_between_the_date(self):
        chars = utils.generate_random_string(size=8)
        start_time_str = utils.insert_str_into_date_part(date_str= self.start_time_str, insert_str= chars)
        self.set_start_date_value_string(start_time_str= start_time_str)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)


    def test_start_date_with_chars_between_the_time(self):
        chars = utils.generate_random_string(size=8)
        start_time_str = utils.insert_str_into_time_part(date_str= self.start_time_str, insert_str= chars)
        self.set_start_date_value_string(start_time_str= start_time_str)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)

    
    def test_start_date_with_multiple_spaces_between_the_date_and_hour(self):
        spaces = " " * random.randint(2, 10)
        start_time_str = utils.insert_str_between_the_date_and_hour(date_str= self.start_time_str, insert_str= spaces)
        self.set_start_date_value_string(start_time_str= start_time_str)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)