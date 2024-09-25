import random
from typing import Any
import time
import string
from .set_up import DiscountCodeCreationTestSetup
import browser_elements
import utils


class TestDiscountCodeText(DiscountCodeCreationTestSetup):

    def run_seccessfull_discount_code_creation_test(self, code: str):
        """ Auxiliar function, this method is NOT consider a test by the unittest lib """
        self.set_discount_code_text(code= code)
        self.click_add_discount_button()
        is_visible = browser_elements.notify_message_alert_success_is_visible(driver= self.driver)
        self.assertTrue(is_visible)

    def run_discount_code_characters_validity_test(self,
                                                   code: str,
                                                   use_javascript: bool,
                                                   assert_msg: Any = None):
        """ Auxiliar function, this method is NOT consider a test by the unittest lib """
        if use_javascript:
            self.set_discount_code_text_using_javascript(code= code)
        else:
            self.set_discount_code_text(code= code)

        self.click_add_discount_button()
        code_input = browser_elements.get_discount_code_input(driver= self.driver)

        self.assert_focus_or_border_color(element= code_input, assert_msg= assert_msg)


    def test_empty_discount_code(self):
        code_input = browser_elements.get_discount_code_input(driver= self.driver)
        code_input.clear()
        self.click_add_discount_button()

        self.assert_focus_or_border_color(element= code_input)

    def test_valid_unique_discount_code(self):
        code = 'uniqueCode' + utils.generate_random_string(size=5)
        self.run_seccessfull_discount_code_creation_test(code= code)
    
    def test_repeated_discount_code(self):
        code = 'repeatedCode' + utils.generate_random_string(size=3)
        self.set_discount_code_text(code= code)
        self.click_add_discount_button()
        time.sleep(1)
        self.setUp()
        
        self.set_discount_code_text(code= code)
        self.click_add_discount_button()

        is_visible = browser_elements.notify_message_alert_danger_is_visible(driver= self.driver)
        self.assertTrue(is_visible)

    
    def test_discount_code_length_equal_to_4(self):
        """ 16 should be the min length allow """
        code = utils.generate_random_string(size=4)
        self.run_seccessfull_discount_code_creation_test(code= code)

    def test_discount_code_length_equal_to_3(self):
        code = utils.generate_random_string(size=3)
        self.run_discount_code_characters_validity_test(code= code, use_javascript= False)

    def test_discount_code_length_equal_to_5(self):
        code = utils.generate_random_string(size=5)
        self.run_seccessfull_discount_code_creation_test(code= code)

    def test_discount_code_length_less_than_4(self):
        size = random.randint(1, 2)
        code = utils.generate_random_string(size=3)
        self.run_discount_code_characters_validity_test(code= code, use_javascript= False)

    def test_discount_code_length_equal_to_16(self):
        """ 16 should be the max length allow """
        code = utils.generate_random_string(size=16)
        self.run_seccessfull_discount_code_creation_test(code= code)

    def test_discount_code_length_equal_to_15(self):
        code = utils.generate_random_string(size=15)
        self.run_seccessfull_discount_code_creation_test(code= code)

    def test_discount_code_length_equal_to_17(self):
        code = utils.generate_random_string(size=17)
        self.run_discount_code_characters_validity_test(code= code, use_javascript= False)

    def test_discount_code_length_greater_than_16(self):
        size = random.randint(18, 40)
        code = utils.generate_random_string(size= size)
        self.run_discount_code_characters_validity_test(code= code, use_javascript= False)


    def test_numbers_only_discount_code(self):
        size = random.randint(4, 16)
        code = utils.generate_random_string(size= size, char_set= string.digits)
        self.run_seccessfull_discount_code_creation_test(code= code)


    def test_lower_case_letters_only_discount_code(self):
        size = random.randint(4, 16)
        code = utils.generate_random_string(size= size, char_set= string.ascii_lowercase)
        self.run_seccessfull_discount_code_creation_test(code= code)

    
    def test_upper_case_letters_only_discount_code(self):
        size = random.randint(4, 16)
        code = utils.generate_random_string(size= size, char_set= string.ascii_uppercase)
        self.run_seccessfull_discount_code_creation_test(code= code)

    def test_letters_only_discount_code(self):
        size = random.randint(8, 16)
        code = utils.generate_random_string(size= size,
                                            char_set= string.ascii_letters
                                            )
        self.run_seccessfull_discount_code_creation_test(code= code)

    def test_letters_and_digist_only_discount_code(self):
        size = random.randint(8, 16)
        code = utils.generate_random_string(size= size)
        self.run_seccessfull_discount_code_creation_test(code= code)


    def test_punctuation_symbols_only_discount_code(self):
        size = random.randint(5, 20)
        code = utils.generate_random_string(size= size, char_set= string.punctuation)
        self.run_discount_code_characters_validity_test(code= code,
                                                        use_javascript= False,
                                                        assert_msg= f"The inputted chars were: {repr(code)}"
                                                        )


    def test_spaces_only_discount_code(self):
        code = " " * random.randint(4, 16)
        self.run_discount_code_characters_validity_test(code= code,
                                                        use_javascript= False,
                                                        assert_msg= f"The inputted chars were: {repr(code)}"
                                                        )
        

    def test_keyboard_newline_only_discount_code(self):
        code = "\n" * random.randint(4, 16)
        self.run_discount_code_characters_validity_test(code= code,
                                                        use_javascript= False,
                                                        assert_msg= f"The inputted chars were: {repr(code)}"
                                                        )
        
    def test_keyboard_carriage_return_only_discount_code(self):
        code = "\r" * random.randint(1, 20)
        self.run_discount_code_characters_validity_test(code= code,
                                                        use_javascript= False,
                                                        assert_msg= f"The inputted chars were: {repr(code)}"
                                                        )
        
    def test_keyboard_vertical_tab_only_discount_code(self):
        code = "\v" * random.randint(1, 20)
        self.run_discount_code_characters_validity_test(code= code,
                                                        use_javascript= False,
                                                        assert_msg= f"The inputted chars were: {repr(code)}"
                                                        )
        
    def test_keyboard_form_feed_only_discount_code(self):
        code = "\f" * random.randint(1, 20)
        self.run_discount_code_characters_validity_test(code= code,
                                                        use_javascript= False,
                                                        assert_msg= f"The inputted chars were: {repr(code)}"
                                                        )
        
    def test_js_inserted_tabs_only_discount_code(self):
        code = "\t" * random.randint(1, 20)
        self.run_discount_code_characters_validity_test(code= code,
                                                        use_javascript= True,
                                                        assert_msg= f"The inputted chars were: {repr(code)}"
                                                        )
    
    def test_js_inserted_newline_only_discount_code(self):
        code = "\n" * random.randint(1, 20)
        self.run_discount_code_characters_validity_test(code= code,
                                                        use_javascript= True,
                                                        assert_msg= f"The inputted chars were: {repr(code)}"
                                                        )
    
    def test_js_inserted_carriage_return_only_discount_code(self):
        code = "\r" * random.randint(1, 20)
        self.run_discount_code_characters_validity_test(code= code,
                                                        use_javascript= True,
                                                        assert_msg= f"The inputted chars were: {repr(code)}"
                                                        )
        
    def test_js_inserted_vertical_tab_only_discount_code(self):
        code = "\v" * random.randint(1, 20)
        self.run_discount_code_characters_validity_test(code= code,
                                                        use_javascript= True,
                                                        assert_msg= f"The inputted chars were: {repr(code)}"
                                                        )
        
    def test_js_inserted_form_feed_only_discount_code(self):
        code = "\f" * random.randint(1, 20)
        self.run_discount_code_characters_validity_test(code= code,
                                                        use_javascript= True,
                                                        assert_msg= f"The inputted chars were: {repr(code)}"
                                                        )

    def test_whitespace_chars_only_discount_code(self):
        size = random.randint(10, 20)
        code = utils.generate_random_string(size= size, char_set=  string.whitespace)
        self.run_discount_code_characters_validity_test(code= code,
                                                        use_javascript= True,
                                                        assert_msg= f"The inputted chars were: {repr(code)}"
                                        )

    def test_discount_code_with_leading_spaces(self):
        code = " " * random.randint(1, 8)
        code = code + utils.generate_random_string(size= 8)
        self.run_discount_code_characters_validity_test(code= code,
                                                        use_javascript= False,
                                                        assert_msg= f"The inputted chars were: {repr(code)}"
                                                        )        

    def test_discount_code_with_trailing_spaces(self):
        code = utils.generate_random_string(size= 8)
        code = code + " " * random.randint(1, 8)
        self.run_discount_code_characters_validity_test(code= code,
                                                        use_javascript= False,
                                                        assert_msg= f"The inputted chars were: {repr(code)}"
                                                        )
        
    def test_discount_code_with_leading_and_trailing_spaces(self):
        code = utils.generate_random_string(size= 8)
        code = " " * random.randint(1, 8) + code + " " * random.randint(1, 8)
        self.run_discount_code_characters_validity_test(code= code,
                                                        use_javascript= False,
                                                        assert_msg= f"The inputted chars were: {repr(code)}"
                                                        )
        
    def test_discount_code_with_leading_whitespace_chars(self):
        whitespace_chars = utils.generate_random_string(size= random.randint(3, 8), char_set=  string.whitespace)
        code = utils.generate_random_string(size= 8)
        code = whitespace_chars + code
        self.run_discount_code_characters_validity_test(code= code,
                                                        use_javascript= True,
                                                        assert_msg= f"The inputted chars were: {repr(code)}"
                                                        )
        
    def test_discount_code_with_trailing_whitespace_chars(self):
        whitespace_chars = utils.generate_random_string(size= random.randint(3, 8), char_set=  string.whitespace)
        code = utils.generate_random_string(size= 8)
        code = code + whitespace_chars
        self.run_discount_code_characters_validity_test(code= code,
                                                        use_javascript= True,
                                                        assert_msg= f"The inputted chars were: {repr(code)}"
                                                        )
        
    def test_discount_code_with_leading_and_trailing_whitespace_chars(self):
        whitespace_chars = utils.generate_random_string(size= random.randint(3, 8), char_set=  string.whitespace)
        code = utils.generate_random_string(size= 8)
        code = whitespace_chars + code + whitespace_chars
        self.run_discount_code_characters_validity_test(code= code,
                                                        use_javascript= True,
                                                        assert_msg= f"The inputted chars were: {repr(code)}"
                                                        )
        
    def test_discount_code_with_spaces_between_the_other_chars(self):
        size = random.randint(8, 16)
        code = utils.generate_random_string(size= size)
        random_index = random.randint(1, len(code)-2)
        temp_list = list(code)
        temp_list[random_index] = " "
        code = "".join(temp_list)
        self.run_discount_code_characters_validity_test(code= code,
                                                        use_javascript= True,
                                                        assert_msg= f"The inputted chars were: {repr(code)}"
                                                        )
        
    
    def test_discount_code_with_punctuation_symbols(self):
        size = random.randint(8, 16)
        random_str = utils.generate_random_string(size= size) + random.choice(string.punctuation)
        random_str = list(random_str)
        random.shuffle(random_str)
        code = "".join(random_str)
        self.run_discount_code_characters_validity_test(code= code,
                                                        use_javascript= False,
                                                        assert_msg= f"The inputted chars were: {repr(code)}"
                                                        )
    

    def test_emoji_only_discount_code(self):
        emojis = "😬💀🧟‍♀️🥶👺🧱🤖🔩🚲🎃🍫🇨🇮🐘🎪👏"
        code = utils.generate_random_string(size=6, char_set= emojis)
        self.run_discount_code_characters_validity_test(code= code,
                                                        use_javascript= True,
                                                        assert_msg= f"The inputted chars were: {repr(code)}"
                                                        )
    
    def test_discount_code_with_emojis(self):
        size = random.randint(8, 16)
        emojis = "😬💀🧟‍♀️🥶👺🧱🤖🔩🚲🎃🍫🇨🇮🐘🎪👏"
        random_str = utils.generate_random_string(size= size) + random.choice(emojis)
        random_str = list(random_str)
        random.shuffle(random_str)
        code = "".join(random_str)
        self.run_discount_code_characters_validity_test(code= code,
                                                        use_javascript= True,
                                                        assert_msg= f"The inputted chars were: {repr(code)}"
                                                        )