import browser_automation
import browser_elements
import browser_scripts
from set_up import BaseAdminPanelTestSetup
import settings
import time


class TestHTMLFooter(BaseAdminPanelTestSetup):
    """ El HTML ingresado debe estar bien formado y puede estar vacío """
    
    def setUp(self) -> None:
        super().setUp()    
    
    def test_valid_html(self):
        code = "<p>Texto footer</p>"
        input = browser_elements.get_input_html_footer(driver= self.driver)
        browser_scripts.set_element_value_attr(driver= self.driver, element= input, value= code)

        btn = browser_elements.get_update_btn_admin_page(driver= self.driver)
        btn.click()
        self.run_test_html_footer_updated_seccessfully()


    def test_html_with_invalid_characters(self):
        code = "<p>Dirección: 1234 Elm St.&<></p>"
        input = browser_elements.get_input_html_footer(driver= self.driver)
        browser_scripts.set_element_value_attr(driver= self.driver, element= input, value= code)

        btn = browser_elements.get_update_btn_admin_page(driver= self.driver)
        btn.click()
        self.run_test_html_footer_update_error()

    
    def test_html_with_unclosed_tags(self):
        code = "<p>Texto sin cerrar"
        input = browser_elements.get_input_html_footer(driver= self.driver)
        browser_scripts.set_element_value_attr(driver= self.driver, element= input, value= code)

        btn = browser_elements.get_update_btn_admin_page(driver= self.driver)
        btn.click()
        self.run_test_html_footer_update_error()

    
    def test_html_without_tags(self):
        code = "Texto sin etiquetas"
        input = browser_elements.get_input_html_footer(driver= self.driver)
        browser_scripts.set_element_value_attr(driver= self.driver, element= input, value= code)

        btn = browser_elements.get_update_btn_admin_page(driver= self.driver)
        btn.click()
        self.run_test_html_footer_update_error()
   

    def test_html_with_empty_tags(self):
        code = "<div></div>"
        input = browser_elements.get_input_html_footer(driver= self.driver)
        browser_scripts.set_element_value_attr(driver= self.driver, element= input, value= code)

        btn = browser_elements.get_update_btn_admin_page(driver= self.driver)
        btn.click()
        self.run_test_html_footer_updated_seccessfully()