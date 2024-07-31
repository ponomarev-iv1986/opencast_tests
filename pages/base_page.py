from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from elements.alert_element import AlertElement


class BasePage:
    def __init__(self, browser: WebDriver):
        self.browser = browser
        self.alert_element = AlertElement(browser)

    # BASE GETTERS
    def get_element(self, locator: tuple, timeout: float = 3.0):
        try:
            return WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            raise AssertionError(
                f"Ждал {timeout} сек. Элемент с локатором {locator} не обнаружен."
            )

    def get_elements(self, locator: tuple, timeout: float = 3.0):
        try:
            return WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )
        except TimeoutException:
            raise AssertionError(
                f"Ждал {timeout} сек. Элементы с локатором {locator} не обнаружены."
            )

    def get_alert(self, timeout: float = 3.0):
        try:
            return WebDriverWait(self.browser, timeout).until(EC.alert_is_present())
        except TimeoutException:
            raise AssertionError("Allert не обнаружен.")

    # BASE ACTIONS
    def click(self, webelement: WebElement):
        ActionChains(self.browser).move_to_element(webelement).pause(
            0.5
        ).click().perform()

    def type(self, webelement: WebElement, text: str):
        ActionChains(self.browser).move_to_element(webelement).pause(
            0.5
        ).click().perform()
        webelement.clear()
        for letter in text:
            webelement.send_keys(letter)

    # BASE ASSERTIONS
    def element_have_text(self, locator: tuple, text: str, timeout: float = 3.0):
        try:
            return WebDriverWait(self.browser, timeout).until(
                EC.text_to_be_present_in_element(locator, text)
            )
        except TimeoutException:
            raise AssertionError(
                f"Ждал {timeout} сек. Текст '{text}' в элементе с "
                f"локатором {locator} не обнаружен."
            )
