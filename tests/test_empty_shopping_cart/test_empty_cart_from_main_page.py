import browser_automation
import browser_elements
from set_up import BaseTestSetup
import settings
import time


class TestEmptyCartFromMainPage(BaseTestSetup):
    
    def setUp(self) -> None:
        super().setUp()
        self.driver.delete_all_cookies()
        self.driver.get(settings.BASE_URL)
    
    def test_empty_cart_with_one_product(self):
        browser_automation.add_product_to_cart_from_main_page(driver= self.driver,
                                                              product_uri= self.simple_product['uri']
                                                              )
        browser_automation.open_shopping_cart_slide_out_panel(driver= self.driver)
        time.sleep(1)
        is_in_cart = browser_automation.check_product_presence_in_cart(driver= self.driver,
                                                                        product_uri= self.simple_product['uri']
                                                                    )
        self.assertTrue(is_in_cart, "The product was NOT present in the cart")

        #time.sleep(1)
        browser_automation.click_empty_shopping_cart(driver= self.driver)
        browser_automation.confirm_empty_cart_operation(driver= self.driver)
        self.run_test_cart_successfully_emptied_message()

        time.sleep(1)
        is_in_cart_2 = browser_automation.check_product_presence_in_cart(driver= self.driver,
                                                                        product_uri= self.simple_product['uri']
                                                                    )
        self.assertFalse(is_in_cart_2, "The cart should be empty")


    def test_empty_cart_with_multiple_products(self):
        for _ in range(3):
            browser_automation.add_product_to_cart_from_main_page(driver= self.driver,
                                                                product_uri= self.simple_product['uri']
                                                                )
        
        browser_automation.open_shopping_cart_slide_out_panel(driver= self.driver)
        time.sleep(1)
        is_in_cart = browser_automation.check_product_presence_in_cart(driver= self.driver,
                                                                        product_uri= self.simple_product['uri']
                                                                    )
        self.assertTrue(is_in_cart, "The product was NOT present in the cart")

        # time.sleep(1)
        browser_automation.click_empty_shopping_cart(driver= self.driver)
        browser_automation.confirm_empty_cart_operation(driver= self.driver)
        self.run_test_cart_successfully_emptied_message()

        time.sleep(1)
        is_in_cart_2 = browser_automation.check_product_presence_in_cart(driver= self.driver,
                                                                        product_uri= self.simple_product['uri']
                                                                    )
        self.assertFalse(is_in_cart_2, "The cart should be empty")
        
    

    def test_cancel_empty_cart_process(self):
        browser_automation.add_product_to_cart_from_main_page(driver= self.driver,
                                                              product_uri= self.simple_product['uri']
                                                              )
        browser_automation.open_shopping_cart_slide_out_panel(driver= self.driver)
        time.sleep(1)
        is_in_cart = browser_automation.check_product_presence_in_cart(driver= self.driver,
                                                                        product_uri= self.simple_product['uri']
                                                                    )
        self.assertTrue(is_in_cart, "The product was NOT present in the cart")

        #time.sleep(1)
        browser_automation.click_empty_shopping_cart(driver= self.driver)
        browser_automation.cancel_empty_cart_operation(driver= self.driver)

        time.sleep(1)
        is_in_cart_2 = browser_automation.check_product_presence_in_cart(driver= self.driver,
                                                                        product_uri= self.simple_product['uri']
                                                                    )
        self.assertTrue(is_in_cart_2, "The cart should be empty")