import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    OPENCART_IMAGE = By.CSS_SELECTOR, "img[title='Your Store']"
    MENU = By.CSS_SELECTOR, "#menu"
    CAROUSEL_BANNER_0 = By.CSS_SELECTOR, "#carousel-banner-0.carousel"
    PRODUCTS = By.CSS_SELECTOR, ".row-cols-xl-4"
    CAROUSEL_BANNER_1 = By.CSS_SELECTOR, "#carousel-banner-1.carousel"
    CURRENCY_SWITCH = By.XPATH, "//span[text()='Currency']"
    CURRENCY_VALUES = By.CSS_SELECTOR, ".dropdown-menu.show>li"
    PRODUCTS_PRICES = By.CSS_SELECTOR, ".price-new"
    _PRODUCTS_XPATH = By.XPATH, "//div[contains(@class, 'row-cols-xl-4')]"

    def _get_product_by_text(self, text: str):
        return self.get_element(
            (By.XPATH, self._PRODUCTS_XPATH[1] + f"//*[text()='{text}']"),
        )

    @allure.step("Открываем главную страницу")
    def open_home_page(self):
        self.open("/")

    # GETTERS
    @allure.step("Ищем логотип Opencart")
    def get_opencart_image(self):
        return self.get_element(self.OPENCART_IMAGE)

    @allure.step("Ищем меню")
    def get_menu(self):
        return self.get_element(self.MENU)

    @allure.step("Ищем верхний баннер")
    def get_carousel_banner_0(self):
        return self.get_element(self.CAROUSEL_BANNER_0)

    @allure.step("Ищем продукты")
    def get_products(self):
        return self.get_element(self.PRODUCTS)

    @allure.step("Ищем нижний баннер")
    def get_carousel_banner_1(self):
        return self.get_element(self.CAROUSEL_BANNER_1)

    @allure.step("Ищем переключатель валют")
    def get_currency_switch(self):
        return self.get_element(self.CURRENCY_SWITCH)

    @allure.step("Ищем значения валют")
    def get_currency_values(self):
        return self.get_elements(self.CURRENCY_VALUES)

    @allure.step("Ищем цены на продукты")
    def get_products_prices(self):
        return self.get_elements(self.PRODUCTS_PRICES)

    # ACTIONS
    @allure.step("Нажимаем на продукт {text}")
    def click_on_product(self, text: str):
        self.click(self._get_product_by_text(text))

    @allure.step("Нажимаем на переключатель валют")
    def click_on_currency_switch(self):
        self.click(self.get_currency_switch())

    @allure.step("Выбираем валюту")
    def select_currency_value_by_index(self, index: int):
        self.click(self.get_currency_values()[index])

    # ASSERTIONS
    @allure.step("Проверяем что валюта соответствует {value}")
    def currency_is(self, value: str):
        assert (
            value in self.get_products_prices()[0].text
        ), f"Валюта не соответствует {value}"
