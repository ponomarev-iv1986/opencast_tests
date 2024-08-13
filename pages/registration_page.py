import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RegistrationPage(BasePage):
    FIRST_NAME_INPUT = By.CSS_SELECTOR, "input[name=firstname]"
    LAST_NAME_INPUT = By.CSS_SELECTOR, "input[name=lastname]"
    EMAIL_INPUT = By.CSS_SELECTOR, "input[name=email]"
    PASSWORD_INPUT = By.CSS_SELECTOR, "input[name=password]"
    SUBMIT_BUTTON = By.CSS_SELECTOR, "button[type=submit]"
    PRIVACY_POLICY_TOGGLE = By.CSS_SELECTOR, ".form-check-input:not(#input-newsletter)"
    SUCCESSFUL_REGISTRATION_MESSAGE = (
        By.XPATH,
        "//div[@id='content']/h1[text()='Your Account Has Been Created!']",
    )

    @allure.step("Открываем страницу регистрации")
    def open_registration_page(self):
        self.open("/index.php?route=account/register")

    # GETTERS
    @allure.step("Ищем поле ввода имени")
    def get_first_name_input(self):
        return self.get_element(self.FIRST_NAME_INPUT)

    @allure.step("Ищем поле ввода фамилии")
    def get_last_name_input(self):
        return self.get_element(self.LAST_NAME_INPUT)

    @allure.step("Ищем поле ввода email")
    def get_email_input(self):
        return self.get_element(self.EMAIL_INPUT)

    @allure.step("Ищем поле ввода пароля")
    def get_password_input(self):
        return self.get_element(self.PASSWORD_INPUT)

    @allure.step("Ищем кнопку подтверждения")
    def get_submit_button(self):
        return self.get_element(self.SUBMIT_BUTTON)

    @allure.step("Ищем переключатель принятия политики приватности")
    def get_privacy_policy_toggle(self):
        return self.get_element(self.PRIVACY_POLICY_TOGGLE)

    @allure.step("Ищем сообщение об успешной регистрации")
    def get_successful_registration_message(self):
        return self.get_element(self.SUCCESSFUL_REGISTRATION_MESSAGE)

    # ACTIONS
    @allure.step("Вводим имя {value}")
    def fill_first_name(self, value):
        self.type(self.get_first_name_input(), value)

    @allure.step("Вводим фамилию {value}")
    def fill_last_name(self, value):
        self.type(self.get_last_name_input(), value)

    @allure.step("Вводим email {value}")
    def fill_email(self, value):
        self.type(self.get_email_input(), value)

    def fill_password(self, value):
        with allure.step("Вводим пароль"):
            self.type(self.get_password_input(), value)

    @allure.step("Принимаем политику приватности")
    def agree_privacy_policy(self):
        self.click(self.get_privacy_policy_toggle())

    @allure.step("Нажимаем кнопку подтверждения")
    def submit(self):
        self.click(self.get_submit_button())
