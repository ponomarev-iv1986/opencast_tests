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

    def open_registration_page(self):
        self.browser.get(self.browser.url + "/index.php?route=account/register")

    # GETTERS
    def get_first_name_input(self):
        return self.get_element(self.FIRST_NAME_INPUT)

    def get_last_name_input(self):
        return self.get_element(self.LAST_NAME_INPUT)

    def get_email_input(self):
        return self.get_element(self.EMAIL_INPUT)

    def get_password_input(self):
        return self.get_element(self.PASSWORD_INPUT)

    def get_submit_button(self):
        return self.get_element(self.SUBMIT_BUTTON)

    def get_privacy_policy_toggle(self):
        return self.get_element(self.PRIVACY_POLICY_TOGGLE)

    def get_successful_registration_message(self):
        return self.get_element(self.SUCCESSFUL_REGISTRATION_MESSAGE)

    # ACTIONS
    def fill_first_name(self, value):
        self.type(self.get_first_name_input(), value)

    def fill_last_name(self, value):
        self.type(self.get_last_name_input(), value)

    def fill_email(self, value):
        self.type(self.get_email_input(), value)

    def fill_password(self, value):
        self.type(self.get_password_input(), value)

    def agree_privacy_policy(self):
        self.click(self.get_privacy_policy_toggle())

    def submit(self):
        self.click(self.get_submit_button())
