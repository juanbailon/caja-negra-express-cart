import browser_automation
import browser_elements
import settings
from dotenv import load_dotenv
import os


def main():
    driver = browser_automation.create_chrome_web_driver_conection()
    driver.get(settings.ADMIN_LOGIN_URL)

    browser_automation.admin_login(driver= driver,
                                   email= os.getenv('ADMIN_EMAIL'),
                                   password= os.getenv('ADMIN_PASSWORD')
                                   )

    browser_automation.wait(2)

    driver.get(settings.ADMIN_CREATE_DISCOUNT_CODE_URL)

    browser_automation.wait(2)

    button = browser_elements.get_add_discount_button(driver= driver)
    button.click()

    browser_automation.wait(1)

    input_element = browser_elements.get_discount_value_input(driver= driver)
    input_element.is_selected()
    border_color = input_element.value_of_css_property("border-color")
    print(type(border_color))
    print(border_color)
    print(border_color=='rgb(204, 65, 53)')

if __name__ == "__main__":
    main()