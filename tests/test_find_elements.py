from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_homepage(browser):
    browser.get(browser.url + "/")
    WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'img[title="Your Store"]'))
    )
    WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#menu"))
    )
    WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#carousel-banner-0.carousel")
        )
    )
    WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".row-cols-xl-4"))
    )
    WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#carousel-banner-1.carousel")
        )
    )


def test_catalog(browser):
    browser.get(browser.url + "/en-gb/catalog/desktops")
    WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//div[@id="content"]/h2[contains(text(), "Desktop")]')
        )
    )
    browser.get(browser.url + "/en-gb/catalog/laptop-notebook")
    WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                '//div[@id="content"]/h2[contains(text(), "Laptops & Notebooks")]',
            )
        )
    )
    browser.get(browser.url + "/en-gb/catalog/component")
    WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//div[@id="content"]/h2[contains(text(), "Components")]')
        )
    )
    browser.get(browser.url + "/en-gb/catalog/tablet")
    WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//div[@id="content"]/h2[contains(text(), "Tablets")]')
        )
    )
    browser.get(browser.url + "/en-gb/catalog/software")
    WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//div[@id="content"]/h2[contains(text(), "Software")]')
        )
    )


def test_shopping_cart(browser):
    browser.get(browser.url + "/en-gb?route=checkout/cart")
    WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'img[title="Your Store"]'))
    )
    WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#menu"))
    )
    WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//div[@id="content"]/h1[contains(text(), "Shopping Cart")]')
        )
    )
    WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                '//div[@id="content"]/p[contains(text(), '
                '"Your shopping cart is empty!")]',
            )
        )
    )
    WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//a[contains(@class, "btn")][contains(text(), "Continue")]')
        )
    )


def test_administration(browser):
    browser.get(browser.url + "/administration")
    WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'img[title="OpenCart"]'))
    )
    WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".card"))
    )
    WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name=username]"))
    )
    WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name=password]"))
    )
    WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type=submit]"))
    )


def test_registration_page(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name=firstname]"))
    )
    WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name=lastname]"))
    )
    WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name=email]"))
    )
    WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name=password]"))
    )
    WebDriverWait(browser, timeout=2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type=submit]"))
    )
