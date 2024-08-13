import allure
from allure_commons.types import Severity
from faker import Faker

from pages.registration_page import RegistrationPage


@allure.title("Проверка регистрации пользователя")
@allure.severity(Severity.CRITICAL)
@allure.tag("TEST", "REGRESS")
@allure.label("owner", "IV_Ponomarev")
@allure.suite("Registration page")
@allure.parent_suite("Opencart")
def test_user_registration(browser):
    registration_page = RegistrationPage(browser)
    fake = Faker()
    registration_page.open_registration_page()
    registration_page.fill_first_name(fake.first_name())
    registration_page.fill_last_name(fake.last_name())
    registration_page.fill_email(fake.email())
    registration_page.fill_password(fake.password())
    registration_page.agree_privacy_policy()
    registration_page.submit()
    registration_page.get_successful_registration_message()
