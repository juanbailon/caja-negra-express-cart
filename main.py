from browser_automation import create_chrome_web_driver_conection
from settings import BASE_URL


def main():
    driver = create_chrome_web_driver_conection()
    driver.get(BASE_URL)



if __name__ == "__main__":
    main()