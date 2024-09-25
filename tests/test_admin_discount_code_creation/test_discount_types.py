from selenium.common.exceptions import NoSuchElementException
from .set_up import DiscountCodeCreationTestSetup
import browser_elements
import browser_automation
import utils


class TestDiscountTypes(DiscountCodeCreationTestSetup):

    def test_valid_discount_types_selection(self):
        for disc_type in self.valid_discount_types:

            browser_automation.select_discount_type(driver= self.driver, discount_type= disc_type)
            current_menu_value = browser_elements.get_discount_type_select_menu(self.driver).get_attribute('value')

            self.assertEqual(current_menu_value, disc_type)

    
    def test_invalid_discount_type_selection(self):
        try:
            discount_type = 'lolcito'
            browser_automation.select_discount_type(driver= self.driver, discount_type= discount_type)
            current_menu_value = browser_elements.get_discount_type_select_menu(self.driver).get_attribute('value')

            self.assertNotEqual(current_menu_value, discount_type)

        except NoSuchElementException as e:
            # option with the provided value could NOT be located, wich is exactly what we are expecting
            pass