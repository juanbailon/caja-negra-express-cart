## ---- Use for type hint ---- ##
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
## --------------------------- ##
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException, NoSuchShadowRootException


def get_login_email_input(driver: WebDriver, element_timeout: int = 5)-> WebElement | None:
    try:
        input_element_username = WebDriverWait(driver, element_timeout).until(
                EC.presence_of_element_located((By.ID, 'email'))
            )
        
        return input_element_username

    except TimeoutException as e:
        return None
    

def get_login_password_input(driver: WebDriver, element_timeout: int = 5)-> WebElement | None:
    try:
        input_element_password = WebDriverWait(driver, element_timeout).until(
                EC.presence_of_element_located((By.ID, 'password'))
            )
        
        return input_element_password

    except TimeoutException as e:
        return None


def get_login_button(driver: WebDriver, element_timeout: int = 5)-> WebElement | None:
    try:
        button = WebDriverWait(driver, element_timeout).until(
            EC.presence_of_element_located((By.ID, "loginForm"))
            )
        
        return button

    except TimeoutException as e:
        return None
    



def get_discount_code_input(driver: WebDriver, element_timeout: int = 5)-> WebElement | None:
    try:
        input_element_discount_code = WebDriverWait(driver, element_timeout).until(
                EC.presence_of_element_located((By.ID, 'discountCode'))
            )
        
        return input_element_discount_code

    except TimeoutException as e:
        return None
    


def get_discount_type_select_menu(driver: WebDriver, element_timeout: int = 5)-> WebElement | None:
    try:
        select_element = WebDriverWait(driver, element_timeout).until(
                EC.presence_of_element_located((By.ID, 'discountType'))
            )
        
        return select_element

    except TimeoutException as e:
        return None
    

def get_discount_value_input(driver: WebDriver, element_timeout: int = 5)-> WebElement | None:
    try:
        input_element_discount_value = WebDriverWait(driver, element_timeout).until(
                EC.presence_of_element_located((By.ID, 'discountValue'))
            )
        
        return input_element_discount_value

    except TimeoutException as e:
        return None
    

def get_discount_start_input(driver: WebDriver, element_timeout: int = 5)-> WebElement | None:
    try:
        input_discount_start = WebDriverWait(driver, element_timeout).until(
                EC.presence_of_element_located((By.ID, 'discountStart'))
            )
        
        return input_discount_start

    except TimeoutException as e:
        return None
    

def get_discount_end_input(driver: WebDriver, element_timeout: int = 5)-> WebElement | None:
    try:
        input_discount_end = WebDriverWait(driver, element_timeout).until(
                EC.presence_of_element_located((By.ID, 'discountEnd'))
            )
        
        return input_discount_end

    except TimeoutException as e:
        return None
    
    

def get_add_discount_button(driver: WebDriver, element_timeout:int = 5)-> WebElement | None:
    try:
        # look for a normal place bet button
        button_element = WebDriverWait(driver, element_timeout).until(
            EC.presence_of_element_located((By.XPATH, "//button[\
                                               contains(@class, 'btn') and\
                                               contains(@class, 'btn-outline-success')]"
                                               ))
            )

        return button_element
        
    except TimeoutException as e:
        return None


def get_notify_message_div(driver: WebDriver, element_timeout:int = 5)-> WebElement | None:
    try:
        div_element = WebDriverWait(driver, element_timeout).until(
                EC.presence_of_element_located((By.ID, 'notify_message'))
            )
        
        return div_element

    except TimeoutException as e:
        return None
    


def notify_message_div_is_visible(driver: WebDriver, element_timeout: int = 5) -> bool:
    try:
        notify_div = WebDriverWait(driver, element_timeout).until(
            EC.visibility_of_element_located((By.ID, "notify_message"))
            )
        
        return True

    except TimeoutException as e:
        return False
    


def notify_message_alert_danger_is_visible(driver: WebDriver, element_timeout: int = 5) -> bool:
    try:
        notify_div = WebDriverWait(driver, element_timeout).until(
            EC.visibility_of_element_located((By.XPATH, "//div[\
                                               @id='notify_message' and\
                                               contains(@class, 'alert-danger')]"
                                               ))
            )
        
        return True

    except TimeoutException as e:
        return False
    

def notify_message_alert_success_is_visible(driver: WebDriver, element_timeout: int = 5) -> bool:
    try:
        notify_div = WebDriverWait(driver, element_timeout).until(
            EC.visibility_of_element_located((By.XPATH, "//div[\
                                               @id='notify_message' and\
                                               contains(@class, 'alert-success')]"
                                               ))
            )
        
        return True

    except TimeoutException as e:
        return False
    

def get_add_to_cart_btn_from_product_page(driver: WebDriver, element_timeout: int = 5) -> WebElement | None:
    try:
        btn = WebDriverWait(driver, element_timeout).until(
            EC.presence_of_element_located((By.XPATH, "//button[\
                                               contains(@class, 'btn') and\
                                               contains(@class, 'btn-primary') and\
                                               contains(@class, 'product-add-to-cart')]"
                                               ))
            )
 
        return btn

    except TimeoutException as e:
        return None
    


def get_product_add_to_cart_btn_from_main_page(driver: WebDriver, product_uri: str, element_timeout:int = 5) -> WebElement | None:
    try:
        thumbnail = WebDriverWait(driver, element_timeout).until(
            EC.presence_of_element_located((By.XPATH, f"//div[\
                                               @class='thumbnail'\
                                                and .//a[@href='{product_uri}']]"
                                               ))
            )
                
        btn = thumbnail.find_element(By.XPATH, ".//a[\
                                                contains(@class, 'btn') and\
                                                contains(@class, 'add-to-cart')]"
                                     ) 
        return btn

    except TimeoutException as e:
        return None
    

def get_cart_contents(driver: WebDriver, element_timeout:int = 5) -> WebElement | None:
    try:
        cart_contents = WebDriverWait(driver, element_timeout).until(
            EC.presence_of_element_located((By.XPATH, "//div[\
                                               contains(@class, 'cart-body')]"
                                               ))
            )
 
        return cart_contents

    except TimeoutException as e:
        return None
    

def get_cart_product_quantity_input(driver: WebDriver, product_uri: str, element_timeout:int = 5) -> WebElement | None:
    cart_contents = get_cart_contents(driver= driver)
    try:
        product_info = WebDriverWait(driver, element_timeout).until(
            lambda x: cart_contents.find_element(By.XPATH, f"//div[@class='row' and .//a[@href='{product_uri}']]")
            )
        
        quantity = WebDriverWait(driver, element_timeout).until(
            lambda x: product_info.find_element(By.XPATH, f"//input[contains(@class, 'cart-product-quantity')]")
            )
 
        return quantity

    except TimeoutException as e:
        return None
    
    

def get_product_quantity_input_from_product_page(driver: WebDriver, element_timeout:int = 5) -> WebElement | None:
    try:
        input = WebDriverWait(driver, element_timeout).until(
            EC.presence_of_element_located((By.ID, 'product_quantity'))
        )
        return input

    except TimeoutException as e:
        return None


def get_shopping_cart_btn(driver: WebDriver, element_timeout:int = 2)-> WebElement | None:
    try:
        a_element = WebDriverWait(driver, element_timeout).until(
            EC.presence_of_element_located((By.XPATH, "//a[\
                                            @href='/checkout/cart' and\
                                            contains(@class, 'btn')]"
                                            ))
        )
        return a_element

    except TimeoutException as e:
        return None
    

def get_empty_shopping_cart_btn(driver: WebDriver, element_timeout:int = 2)-> WebElement | None:
    try:
        btn = WebDriverWait(driver, element_timeout).until(
            EC.presence_of_element_located((By.XPATH, "//button[\
                                            @id='empty-cart']"
                                            ))
        )
        return btn

    except TimeoutException as e:
        return None
    

def get_first_visible_modal_dialog(driver: WebDriver, element_timeout:int = 2)-> WebElement | None:
    try:
        dialog_element = WebDriverWait(driver, element_timeout).until(
            EC.visibility_of_element_located((By.XPATH, "//div[\
                                            @class='modal-dialog']"
                                            ))
        )
        return dialog_element

    except TimeoutException as e:
        return None
    


def get_input_html_footer(driver: WebDriver, element_timeout:int = 3)-> WebElement | None:
    try:
        input = WebDriverWait(driver, element_timeout).until(
            EC.presence_of_element_located((By.ID, 'footerHtml_input'))
        )
        return input

    except TimeoutException as e:
        return None
    

def get_update_btn_admin_page(driver: WebDriver, element_timeout:int = 3)-> WebElement | None:
    try:
        btn = WebDriverWait(driver, element_timeout).until(
            EC.presence_of_element_located((By.ID, 'btnSettingsUpdate'))
        )
        return btn

    except TimeoutException as e:
        return None
    

def get_SMTP_host_input(driver: WebDriver, element_timeout:int = 3)-> WebElement | None:
    try:
        input = WebDriverWait(driver, element_timeout).until(
            EC.presence_of_element_located((By.NAME, 'emailHost'))
        )
        return input

    except TimeoutException as e:
        return None
    

def get_SMTP_port_input(driver: WebDriver, element_timeout:int = 3)-> WebElement | None:
    try:
        input = WebDriverWait(driver, element_timeout).until(
            EC.presence_of_element_located((By.NAME, 'emailPort'))
        )
        return input

    except TimeoutException as e:
        return None
    

def get_SMTP_username_input(driver: WebDriver, element_timeout:int = 3)-> WebElement | None:
    try:
        input = WebDriverWait(driver, element_timeout).until(
            EC.presence_of_element_located((By.NAME, 'emailUser'))
        )
        return input

    except TimeoutException as e:
        return None
    

def get_SMTP_password_input(driver: WebDriver, element_timeout:int = 3)-> WebElement | None:
    try:
        input = WebDriverWait(driver, element_timeout).until(
            EC.presence_of_element_located((By.NAME, 'emailPassword'))
        )
        return input

    except TimeoutException as e:
        return None
    

def get_SMTP_email_secure_checkbox(driver: WebDriver, element_timeout:int = 3)-> WebElement | None:
    try:
        input = WebDriverWait(driver, element_timeout).until(
            EC.presence_of_element_located((By.NAME, 'emailSecure'))
        )
        return input

    except TimeoutException as e:
        return None