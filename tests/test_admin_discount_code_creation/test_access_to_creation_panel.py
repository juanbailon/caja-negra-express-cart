from .set_up import BaseAdminPanelTestSetup
import settings
import browser_elements

class TestAccestoToPanelAndSendEmptyForm(BaseAdminPanelTestSetup):
    
    def test_access_to_admin_discount_codes_panel(self):        
        self.assertEqual(self.driver.title, "Discount code create")
        self.assertEqual(self.driver.current_url, settings.ADMIN_CREATE_DISCOUNT_CODE_URL)

    def test_send_empty_form(self):
        button = browser_elements.get_add_discount_button(driver= self.driver)
        button.click()

        is_visible = browser_elements.notify_message_div_is_visible(driver= self.driver)
        self.assertFalse(is_visible)