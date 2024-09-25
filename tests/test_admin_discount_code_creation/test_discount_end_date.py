import random
import string
from datetime import datetime, timedelta
from .set_up import DiscountCodeCreationTestSetup
import browser_elements
import utils


class TestDiscountCodeEndDate(DiscountCodeCreationTestSetup):

        
    def run_website_end_time_equal_to_test(self, end_time: datetime|str):
        """ Auxiliar function, this method is NOT consider a test by the unittest lib """
        if isinstance(end_time, datetime):
            end_time_str = utils.parse_datetime_to_european_format(end_time)
        else:
            end_time_str = end_time

        website_end_time = browser_elements.get_discount_end_input(self.driver).get_attribute('value')
        self.assertEqual(website_end_time, end_time_str)

    
    def run_website_end_time_NOT_equal_to_test(self, end_time: datetime):
        """ Auxiliar function, this method is NOT consider a test by the unittest lib """
        website_end_time = browser_elements.get_discount_end_input(self.driver).get_attribute('value')
        end_time_str = utils.parse_datetime_to_european_format(end_time)
        self.assertNotEqual(website_end_time, end_time_str)


    def test_valid_end_date(self):
        end_time = datetime.now() + timedelta(days= 10)
        self.set_end_date_value(end_time= end_time)
        self.run_website_end_time_equal_to_test(end_time= end_time)
        self.click_add_discount_button()

        is_visible = browser_elements.notify_message_alert_success_is_visible(driver= self.driver)
        self.assertTrue(is_visible)

    def test_end_date_equal_to_now(self):
        end_time = datetime.now()
        self.set_end_date_value(end_time= end_time)
        self.run_website_end_time_equal_to_test(end_time= end_time)
        
        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)


    def test_end_date_is_a_past_date(self):
        end_time = datetime.now() - timedelta(days= 1)
        self.set_end_date_value(end_time= end_time)
        self.run_website_end_time_equal_to_test(end_time= end_time)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)

    
    def test_end_date_is_greater_than_now_for_lees_than_a_day(self):
        start_time = datetime.now() + timedelta(hours= 1)
        self.set_start_date_value(start_time= start_time)
        end_time = datetime.now() + timedelta(hours= 15)
        self.set_end_date_value(end_time= end_time)
        self.run_website_end_time_equal_to_test(end_time= end_time)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_success_is_visible(driver= self.driver)
        self.assertTrue(is_visible)

    def test_end_date_is_greater_than_now_for_exactly_a_day(self):
        start_time = datetime.now() + timedelta(hours=5)
        self.set_start_date_value(start_time= start_time)
        end_time = datetime.now() + timedelta(days= 1)
        self.set_end_date_value(end_time= end_time)
        self.run_website_end_time_equal_to_test(end_time= end_time)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_success_is_visible(driver= self.driver)
        self.assertTrue(is_visible)


    def test_end_date_is_before_the_start_date(self):
        start_time = datetime.now() + timedelta(days= 10)
        self.set_start_date_value(start_time= start_time)
        end_time = self.end_time + timedelta(days= 5)
        self.set_end_date_value(end_time= end_time)
        self.run_website_end_time_equal_to_test(end_time= end_time)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)


    def test_end_date_with_trailing_whitespace_chars(self):
        trailing_size = random.randint(3, 8)
        whitespaces = utils.generate_random_string(size= trailing_size, char_set= string.whitespace)
        end_time_str = self.end_time_str + whitespaces
        self.set_end_date_value_string(end_time_str= end_time_str)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)


    def test_end_date_with_leading_whitespace_chars(self):
        leading_size = random.randint(3, 8)
        whitespaces = utils.generate_random_string(size= leading_size, char_set= string.whitespace)
        end_time_str = whitespaces + self.end_time_str
        self.set_end_date_value_string(end_time_str= end_time_str)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)


    def test_end_date_with_leading_and_trailing_whitespace_chars(self):
        size = random.randint(3, 8)
        leading = utils.generate_random_string(size= size, char_set= string.whitespace)
        trailing = utils.generate_random_string(size= size, char_set= string.whitespace)
        end_time_str = leading + self.end_time_str + trailing
        self.set_end_date_value_string(end_time_str= end_time_str)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)
        
        
    def test_end_date_is_invalid_date(self):
        start_time_str = "12/11/2100 13:00"
        end_time_str = "20/14/2100 14:30"
        self.set_start_date_value_string(start_time_str= start_time_str)
        self.set_end_date_value_string(end_time_str= end_time_str)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)


    def test_end_date_with_invalid_hour(self):
        start_time_str = "31/11/2100 3:20"
        end_time_str = "10/12/2100 41:30"
        self.set_start_date_value_string(start_time_str= start_time_str)
        self.set_end_date_value_string(end_time_str= end_time_str)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)

    def test_end_date_with_invalid_minute(self):
        start_time_str = "31/11/2100 2:00"
        end_time_str = "10/12/2100 14:73"
        self.set_start_date_value_string(start_time_str= start_time_str)
        self.set_end_date_value_string(end_time_str= end_time_str)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)

    
    def test_end_date_without_an_specific_hour(self):
        date_part, time_part = self.end_time_str.split(' ')
        end_time_str = date_part
        self.set_end_date_value_string(end_time_str= end_time_str)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)

    
    def test_end_date_with_chars_between_the_date_and_hour(self):
        chars = utils.generate_random_string(size=8)
        end_time_str = utils.insert_str_between_the_date_and_hour(date_str= self.end_time_str, insert_str= chars)
        self.set_end_date_value_string(end_time_str= end_time_str)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)

    
    def test_end_date_with_letters_only(self):
        size = random.randint(5, 20)
        end_time_str = utils.generate_random_string(size= size, char_set= string.ascii_letters) 
        self.set_end_date_value_string(end_time_str= end_time_str)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)


    def test_end_date_with_numbers_only(self):
        size = random.randint(5, 20)
        end_time_str = utils.generate_random_string(size= size, char_set=string.digits) 
        self.set_end_date_value_string(end_time_str= end_time_str)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)


    def test_end_date_with_whitespace_chars_only(self):
        size = random.randint(5, 20)
        end_time_str = utils.generate_random_string(size= size, char_set=string.whitespace) 
        self.set_end_date_value_string(end_time_str= end_time_str)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)


    def test_end_date_with_punctiation_chars_only(self):
        size = random.randint(5, 20)
        end_time_str = utils.generate_random_string(size= size, char_set=string.punctuation) 
        self.set_end_date_value_string(end_time_str= end_time_str)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)


    def test_end_date_with_trailing_chars(self):
        trailing_size = random.randint(5, 15)
        trailing_chars = utils.generate_random_string(size= trailing_size, char_set= string.printable)
        end_time_str = self.end_time_str + trailing_chars
        self.set_end_date_value_string(end_time_str= end_time_str)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)


    def test_end_date_with_leading_chars(self):
        leadingsize = random.randint(5, 15)
        char_set = string.ascii_letters + string.digits + string.punctuation
        leading_chars = utils.generate_random_string(size= leadingsize, char_set= char_set )
        end_time_str = leading_chars + self.end_time_str
        self.set_end_date_value_string(end_time_str= end_time_str)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)


    def test_end_date_with_leading_and_trailing_chars(self):
        size = random.randint(5, 15)
        leading_chars = utils.generate_random_string(size= size, char_set= string.printable)
        trailing_chars = utils.generate_random_string(size= size, char_set= string.printable)
        end_time_str = leading_chars + self.end_time_str + trailing_chars
        self.set_end_date_value_string(end_time_str= end_time_str)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)


    def test_end_date_with_chars_between_the_date(self):
        chars = utils.generate_random_string(size= random.randint(1, 10))
        end_time_str = utils.insert_str_into_date_part(date_str= self.end_time_str, insert_str= chars)
        self.set_end_date_value_string(end_time_str= end_time_str)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)


    def test_end_date_with_chars_between_the_time(self):
        chars = utils.generate_random_string(size= random.randint(1, 10))
        end_time_str = utils.insert_str_into_time_part(date_str= self.end_time_str, insert_str= chars)
        self.set_end_date_value_string(end_time_str= end_time_str)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)

    
    def test_end_date_with_multiple_spaces_between_the_date_and_hour(self):
        spaces = " " * random.randint(2, 10)
        end_time_str = utils.insert_str_between_the_date_and_hour(date_str= self.end_time_str, insert_str= spaces)
        self.set_end_date_value_string(end_time_str= end_time_str)

        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)