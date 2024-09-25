from typing import Any
import json
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import JavascriptException
import utils


SCRIPT_SET_ELEMENT_VALUE_ATTRIBUTE = "arguments[0].value = '{value}';"


def set_element_value_attr(driver: WebDriver, element: WebElement, value: str, use_json_dumps= False):
    """
    Set the value attribute of an input element using JavaScript with proper escaping.
    
    :param driver: Selenium WebDriver instance
    :param element: WebElement to set the value for
    :param value: The value to set (can include special characters)
    """
    # escaped_value = json.dumps(value)
    escaped_value = utils.escape_js_string(value= value)

    script = SCRIPT_SET_ELEMENT_VALUE_ATTRIBUTE.format(value= escaped_value)
    try:
        driver.execute_script(script, element)

    except JavascriptException as e:
        raise e