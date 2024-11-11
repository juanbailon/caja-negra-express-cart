import time
from datetime import datetime
from selenium import webdriver
## ---- Use for type hint ---- ##
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
## --------------------------- ##
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import browser_elements
import utils
import browser_scripts



def create_chrome_web_driver_conection(headless:bool = False,
                                       detach:bool = False,
                                       use_sandbox: bool = True,
                                       use_dev_shm: bool = True,
                                       window_width: int = 1052,
                                       window_height: int = 825                                     
                                       ) -> WebDriver:

    service = Service(ChromeDriverManager().install())
    options = Options()
    options.add_experimental_option("detach", detach)
    options.add_argument(f"--window-size={window_width},{window_height}")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-renderer-backgrounding")
    options.page_load_strategy = 'normal'

    if not use_sandbox:
        options.add_argument('--no-sandbox')
    if not use_dev_shm:
        options.add_argument('--disable-dev-shm-usage')
    if headless:
        options.add_argument("--headless=new")

    driver = webdriver.Chrome(service= service, options=options)

    return driver


def quit_driver_conection(driver: WebDriver):
    driver.quit()

def open_url(driver: WebDriver, url: str):
    driver.get(url)

def wait(seconds: int|float):
    time.sleep(seconds)


def admin_login(driver: WebDriver, email: str, password: str):

    emial_input =  browser_elements.get_login_email_input(driver= driver)
    password_input = browser_elements.get_login_password_input(driver= driver)
    login_button = browser_elements.get_login_button(driver= driver)

    emial_input.send_keys(email)
    password_input.send_keys(password)
    login_button.click()


def select_discount_type(driver: WebDriver, discount_type: str):
    # if discount_type not in ('percent', 'amount'):
    #     raise ValueError(f"{type} is NOT a valid discount type. The only valid values are ['percent', 'amount']")
    
    select_menu = Select( browser_elements.get_discount_type_select_menu(driver= driver) )
    select_menu.select_by_value(discount_type)


def set_discount_start_time_value(driver: WebDriver, start_time: datetime):
    start_date_element = browser_elements.get_discount_start_input(driver= driver)

    start_time_str = utils.parse_datetime_to_european_format(start_time)

    browser_scripts.set_element_value_attr(driver= driver,
                                            element= start_date_element,
                                            value= start_time_str
                                        )
    

def set_discount_end_time_value(driver: WebDriver, end_time: datetime):
    end_date_element = browser_elements.get_discount_end_input(driver= driver)

    end_time_str = utils.parse_datetime_to_european_format(end_time)

    browser_scripts.set_element_value_attr(driver= driver,
                                            element= end_date_element,
                                            value= end_time_str
                                        )


def check_product_presence_in_cart(driver: WebDriver, product_uri: str) -> bool:
    cart_contents =  browser_elements.get_cart_contents(driver= driver)
    try:
        cart_contents.find_element(By.XPATH, f"//div[@class='row']//a[@href='{product_uri}']")
        return True
    
    except NoSuchElementException as e:
        return False


def check_product_quantity_in_cart(driver: WebDriver, product_uri: str) -> int | None:
    quantity =  browser_elements.get_cart_product_quantity_input(driver= driver, product_uri= product_uri)

    return int(quantity.get_attribute('value'))
