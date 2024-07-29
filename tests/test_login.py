import os

import dotenv
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_login_administration(browser):
    dotenv.load_dotenv()
    browser.get(browser.url + "/administration")
    username = WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name=username]"))
    )
    password = WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name=password]"))
    )
    username.send_keys(os.getenv("LOGIN"))
    password.send_keys(os.getenv("PASSWORD") + Keys.ENTER)
    WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//span[contains(text(), "John Doe")]')
        )
    )
