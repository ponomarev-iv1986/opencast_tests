import logging

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
        self.__config_logger()

    # CONFIG LOGGER
    def __config_logger(self):
        self.logger = logging.getLogger(type(self).__name__)
        handler = logging.StreamHandler()
        handler.setFormatter(
            logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        )
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.DEBUG)

    # OPEN PAGE
    def open(self, url: str):
        self.logger.info(f"Open {self.browser.url + url}")
        self.browser.get(self.browser.url + url)

    # BASE GETTERS
    def get_element(self, locator: tuple, timeout: float = 3.0):
        self.logger.info(f"Get element {locator}")
        try:
            return WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            raise AssertionError(
                f"Ждал {timeout} сек. Элемент с локатором {locator} не обнаружен."
            )

    def get_elements(self, locator: tuple, timeout: float = 3.0):
        self.logger.info(f"Get elements {locator}")
        try:
            return WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )
        except TimeoutException:
            raise AssertionError(
                f"Ждал {timeout} сек. Элементы с локатором {locator} не обнаружены."
            )

    def get_alert(self, timeout: float = 3.0):
        self.logger.info("Get alert")
        try:
            return WebDriverWait(self.browser, timeout).until(EC.alert_is_present())
        except TimeoutException:
            raise AssertionError(f"Ждал {timeout} сек. Alert не обнаружен.")

    # BASE ACTIONS
    def click(self, webelement: WebElement):
        self.logger.info(f"Click {webelement}")
        ActionChains(self.browser).move_to_element(webelement).pause(
            0.5
        ).click().perform()

    def type(self, webelement: WebElement, text: str):
        self.logger.info(f"Type '{text}' into {webelement}")
        ActionChains(self.browser).move_to_element(webelement).pause(
            0.5
        ).click().perform()
        webelement.clear()
        for letter in text:
            webelement.send_keys(letter)

    # BASE ASSERTIONS
    def element_have_text(self, locator: tuple, text: str, timeout: float = 3.0):
        self.logger.info(f"Assert that element {locator} have text {text}")
        try:
            return WebDriverWait(self.browser, timeout).until(
                EC.text_to_be_present_in_element(locator, text)
            )
        except TimeoutException:
            raise AssertionError(
                f"Ждал {timeout} сек. Текст '{text}' в элементе с "
                f"локатором {locator} не обнаружен."
            )
