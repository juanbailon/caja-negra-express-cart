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