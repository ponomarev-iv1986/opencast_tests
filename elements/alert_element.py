from selenium.common import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class AlertElement:
    ALERT_ELEMENT = By.CSS_SELECTOR, "#container #alert"

    def __init__(self, browser: WebDriver):
        self.browser = browser

    def have_text(self, value: str):
        try:
            WebDriverWait(self.browser, timeout=3).until(
                EC.text_to_be_present_in_element(self.ALERT_ELEMENT, value)
            )
        except TimeoutException:
            raise AssertionError(
                f"В элементе {self.ALERT_ELEMENT} не найден текст '{value}'"
            )
