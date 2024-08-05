import time

import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):
    ADD_TO_CART_BUTTON = By.CSS_SELECTOR, "button#button-cart"

    # GETTERS
    @allure.step("Ищем кнопку добавления в корзину")
    def get_add_to_cart_button(self):
        return self.get_element(self.ADD_TO_CART_BUTTON)

    # ACTIONS
    @allure.step("Нажимаем не кнопку добавления в корзину")
    def add_to_shopping_cart(self):
        self.click(self.get_add_to_cart_button())
        time.sleep(0.5)
