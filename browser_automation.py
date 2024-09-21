import time
from selenium import webdriver
## ---- Use for type hint ---- ##
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
## --------------------------- ##
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager



def create_chrome_web_driver_conection(
                                       detach:bool = True,
                                       use_sandbox: bool = True,
                                       use_dev_shm: bool = True,                                       
                                       ) -> WebDriver:

    service = Service(ChromeDriverManager().install())
    options = Options()
    options.add_experimental_option("detach", detach)
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-renderer-backgrounding")
    options.page_load_strategy = 'normal'

    if not use_sandbox:
        options.add_argument('--no-sandbox')
    if not use_dev_shm:
        options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service= service, options=options)

    return driver


def quit_driver_conection(driver: WebDriver):
    driver.quit()

def open_url(driver: WebDriver, url: str):
    driver.get(url)

def wait(seconds: int|float):
    time.sleep(seconds)