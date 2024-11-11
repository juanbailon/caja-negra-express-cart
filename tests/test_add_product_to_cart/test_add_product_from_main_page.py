from datetime import datetime, timedelta
import browser_automation
import browser_elements
from set_up import BaseTestAvailableProduct, BaseTestNotAvailableProduct
import settings


class TestAvailableProductInMainPage(BaseTestAvailableProduct):
    
    def setUp(self) -> None:
        super().setUp()
        self.driver.get(settings.BASE_URL)
    
    def test_add_to_cart_simple_product(self):
        btn = browser_elements.get_product_add_to_cart_btn_from_main_page(driver= self.driver,
                                                                          product_uri= self.simple_product['uri']
                                                                        )
        btn.click()
        self.run_test_product_added_to_cart_successfully_message()

        is_in_cart = browser_automation.check_product_presence_in_cart(driver= self.driver,
                                                                        product_uri= self.simple_product['uri']
                                                                    )
        self.assertTrue(is_in_cart, "The product was NOT present in the cart")

        quantity = browser_automation.check_product_quantity_in_cart(driver= self.driver,
                                                          product_uri= self.simple_product['uri'])
        
        self.assertEqual(1, quantity)

    
    def test_add_to_cart_product_with_variants(self):
        uri = self.product_with_variants['uri']
        btn = browser_elements.get_product_add_to_cart_btn_from_main_page(driver= self.driver,
                                                                          product_uri= uri
                                                                        )
        btn.click()
        self.assertEqual(self.driver.current_url, settings.BASE_URL+uri)



class TestNotAvailableProductInMainPage(BaseTestNotAvailableProduct):
    def setUp(self) -> None:
        super().setUp()
        self.driver.get(settings.BASE_URL)

    # this test a draft product (unavailable product)
    def test_add_to_cart_draft_product(self):
        uri = self.not_available_product['uri']
        btn = browser_elements.get_product_add_to_cart_btn_from_main_page(driver= self.driver,
                                                                          product_uri= uri
                                                                        )
        self.run_test_product_addition_to_cart_failed_message()
        self.assertIsNone(btn, "The product shoudl NOT be display")
   

        


    