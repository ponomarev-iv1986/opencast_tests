from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_add_to_shopping_cart(browser):
    browser.get(browser.url + "/")
    product = WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".product-thumb"))
    )[0]
    product.click()
    button = WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "button#button-cart"))
    )
    button.click()
    WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//button[contains(text(), "1 item(s)")]')
        )
    )
