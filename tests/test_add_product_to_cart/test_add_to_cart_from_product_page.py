from datetime import datetime, timedelta
import browser_automation
import browser_elements
import browser_scripts
from set_up import BaseTestAvailableProduct, BaseTestNotAvailableProduct
import settings
import utils
import time

class TestAvailableInProductPage(BaseTestAvailableProduct):
    
    def setUp(self) -> None:
        super().setUp()
        self.driver.delete_all_cookies()
        self.driver.get(self.simple_product['url'])

    
    def test_add_to_cart_simple_product(self):
        btn = browser_elements.get_add_to_cart_btn_from_product_page(driver= self.driver)
        btn.click()
        self.run_test_product_added_to_cart_successfully_message()

        is_in_cart = browser_automation.check_product_presence_in_cart(driver= self.driver,
                                                                        product_uri= self.simple_product['uri']
                                                                    )
        self.assertTrue(is_in_cart, "The product was NOT present in the cart")

        quantity = browser_automation.check_product_quantity_in_cart(driver= self.driver,
                                                          product_uri= self.simple_product['uri'])
        
        self.assertEqual(1, quantity)

    
    def test_quantity_greater_than_one_simple_product(self):
        quantity_input = browser_elements.get_product_quantity_input_from_product_page(driver= self.driver)
        amount = 12
        quantity_input.clear()
        quantity_input.send_keys(amount)

        btn = browser_elements.get_add_to_cart_btn_from_product_page(driver= self.driver)
        btn.click()
        self.run_test_product_added_to_cart_successfully_message()

        is_in_cart = browser_automation.check_product_presence_in_cart(driver= self.driver,
                                                                        product_uri= self.simple_product['uri']
                                                                    )
        self.assertTrue(is_in_cart, "The product was NOT present in the cart")

        quantity_cart = browser_automation.check_product_quantity_in_cart(driver= self.driver,
                                                          product_uri= self.simple_product['uri'])
        
        self.assertEqual(amount, quantity_cart)


    def test_quantity_equal_to_zero_simple_product(self):
        quantity_input = browser_elements.get_product_quantity_input_from_product_page(driver= self.driver)
        amount = 0
        quantity_input.clear()
        quantity_input.send_keys(amount)

        btn = browser_elements.get_add_to_cart_btn_from_product_page(driver= self.driver)
        btn.click()
        self.run_test_product_addition_to_cart_failed_message()


    def test_quantity_less_than_zero_simple_product(self):
        quantity_input = browser_elements.get_product_quantity_input_from_product_page(driver= self.driver)
        amount = -1
        quantity_input.clear()
        quantity_input.send_keys(amount)

        btn = browser_elements.get_add_to_cart_btn_from_product_page(driver= self.driver)
        btn.click()
        self.run_test_product_addition_to_cart_failed_message()
        

    def test_add_multiple_products_one_at_the_time_simple_product(self):
        btn = browser_elements.get_add_to_cart_btn_from_product_page(driver= self.driver)
        btn.click()
        self.run_test_product_added_to_cart_successfully_message()

        time.sleep(1.5)
        btn.click()
        self.run_test_product_added_to_cart_successfully_message()

        is_in_cart = browser_automation.check_product_presence_in_cart(driver= self.driver,
                                                                        product_uri= self.simple_product['uri']
                                                                    )
        self.assertTrue(is_in_cart, "The product was NOT present in the cart")

        quantity = browser_automation.check_product_quantity_in_cart(driver= self.driver,
                                                          product_uri= self.simple_product['uri'])
        
        self.assertEqual(2, quantity)


    def test_quantity_greater_than_stock(self):
        self.driver.get(self.product_with_variants['url'])
        quantity_input = browser_elements.get_product_quantity_input_from_product_page(driver= self.driver)
        amount = self.product_with_variants['stock'] + 1
        quantity_input.clear()
        quantity_input.send_keys(amount)

        btn = browser_elements.get_add_to_cart_btn_from_product_page(driver= self.driver)
        btn.click()
        self.run_test_product_addition_to_cart_failed_message()



class TestNotAvailableInProductPage(BaseTestNotAvailableProduct):
    
    def setUp(self) -> None:
        super().setUp()
        self.driver.delete_all_cookies()
        self.driver.get(self.not_available_product['url'])

    def test_add_to_cart_simple_product(self):
        btn = browser_elements.get_add_to_cart_btn_from_product_page(driver= self.driver, element_timeout=3)
        
        self.assertIsNone(btn, "The product should NOT be accesible")