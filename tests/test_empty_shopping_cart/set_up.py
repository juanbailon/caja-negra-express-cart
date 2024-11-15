import unittest
import browser_automation
import browser_elements
import settings
import utils
import time

class BaseTestSetup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Setup code that runs once for all tests
        cls.driver = browser_automation.create_chrome_web_driver_conection(headless= settings.IS_HEADLESS)
        
        cls.product_with_variants = {
            'name': 'producto 1',
            'uri': '/product/product-1',
            'url': f'{settings.BASE_URL}/product/product-1',
            'price': 10,
            'option': 'one',
            'stock': 10
        }
        cls.simple_product = {
            'name': 'producto 2',
            'uri': '/product/product-2',
            'url': f'{settings.BASE_URL}/product/product-2',
            'price': 20, 
        }
        cls.not_available_product = {
            'name': 'producto A',
            'uri': '/product/product-a',
            'url': f'{settings.BASE_URL}/product/product-a',
            'price': 50
        }

    @classmethod
    def tearDownClass(cls):
        # Cleanup code that runs once after all tests
        #cls.driver.quit()  # Close the browser driver
        pass


    def run_test_cart_successfully_emptied_message(self):
        is_visible = browser_elements.notify_message_alert_success_is_visible(driver= self.driver, element_timeout=3)
        self.assertTrue(is_visible, "Success message was NOT display")
