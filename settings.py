from dotenv import load_dotenv
import os

IS_HEADLESS = os.getenv('IS_HEADLESS').lower() == 'true'

ADMIN_EMAIL = os.getenv('ADMIN_EMAIL')

ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')

BASE_URL = "http://localhost:1111"

ADMIN_LOGIN_URL = BASE_URL + "/admin/login"

ADMIN_CREATE_DISCOUNT_CODE_URL = BASE_URL + "/admin/settings/discount/new"

ADMIN_SETTINGS_URL = BASE_URL + "/admin/settings"