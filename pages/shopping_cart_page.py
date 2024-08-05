from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ShoppingCartPage(BasePage):
    OPENCART_IMAGE = By.CSS_SELECTOR, "img[title='Your Store']"
    MENU = By.CSS_SELECTOR, "#menu"
    SHOPPING_CART_TITLE = (
        By.XPATH,
        "//div[@id='content']/h1[contains(text(), 'Shopping Cart')]",
    )
    EMPTY_SHOPPING_CART_TITLE = (
        By.XPATH,
        "//div[@id='content']/p[contains(text(), 'Your shopping cart is empty!')]",
    )
    CONTINUE_BUTTON = (
        By.XPATH,
        "//a[contains(@class, 'btn')][contains(text(), 'Continue')]",
    )
    PRODUCTS = By.CSS_SELECTOR, ".table-bordered:not(.mb-2)"

    def open_shopping_cart_page(self):
        self.browser.get(self.browser.url + "/en-gb?route=checkout/cart")

    # GETTERS
    def get_opencart_image(self):
        return self.get_element(self.OPENCART_IMAGE)

    def get_menu(self):
        return self.get_element(self.MENU)

    def get_shopping_cart_title(self):
        return self.get_element(self.SHOPPING_CART_TITLE)

    def get_empty_shopping_cart_title(self):
        return self.get_element(self.EMPTY_SHOPPING_CART_TITLE)

    def get_continue_button(self):
        return self.get_element(self.CONTINUE_BUTTON)

    # ASSERTIONS
    def have_product(self, product_name: str):
        try:
            self.element_have_text(self.PRODUCTS, product_name)
        except AssertionError:
            raise AssertionError(f"Продукта {product_name} нет в корзине")
