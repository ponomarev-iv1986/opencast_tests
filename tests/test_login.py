import os

import allure
import dotenv
from allure_commons.types import Severity

from pages.admin_page import AdminPage


@allure.title("Проверка логина на странице администрирования")
@allure.severity(Severity.CRITICAL)
@allure.tag("TEST", "REGRESS")
@allure.label("owner", "IV_Ponomarev")
@allure.suite("Administration page")
@allure.parent_suite("Opencart")
def test_login_administration(browser):
    dotenv.load_dotenv()
    admin_page = AdminPage(browser)
    admin_page.open_admin_page()
    admin_page.fill_username(os.getenv("LOGIN"))
    admin_page.fill_password(os.getenv("PASSWORD"))
    admin_page.submit()
    admin_page.get_profile_name()
