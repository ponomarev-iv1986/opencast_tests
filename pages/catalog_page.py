import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CatalogPage(BasePage):
    DESKTOPS_CONTENT_TITLE = (
        By.XPATH,
        "//div[@id='content']/h2[contains(text(), 'Desktops')]",
    )
    LAPTOPS_AND_NOTEBOOKS_CONTENT_TITLE = (
        By.XPATH,
        "//div[@id='content']/h2[contains(text(), 'Laptops & Notebooks')]",
    )
    COMPONENTS_CONTENT_TITLE = (
        By.XPATH,
        "//div[@id='content']/h2[contains(text(), 'Components')]",
    )
    TABLETS_CONTENT_TITLE = (
        By.XPATH,
        "//div[@id='content']/h2[contains(text(), 'Tablets')]",
    )
    SOFTWARE_CONTENT_TITLE = (
        By.XPATH,
        "//div[@id='content']/h2[contains(text(), 'Software')]",
    )

    @allure.step("Открываем страницу с компьютерами")
    def open_desktops_page(self):
        self.open("/en-gb/catalog/desktops")

    @allure.step("Открываем страницу с ноутбуками")
    def open_laptops_and_notebooks_page(self):
        self.open("/en-gb/catalog/laptop-notebook")

    @allure.step("Открываем страницу с компонентами")
    def open_components_page(self):
        self.open("/en-gb/catalog/component")

    @allure.step("Открываем страницу с планшетами")
    def open_tablets_page(self):
        self.open("/en-gb/catalog/tablet")

    @allure.step("Открываем страницу с программным обеспечением")
    def open_software_page(self):
        self.open("/en-gb/catalog/software")

    # GETTERS
    @allure.step("Ищем заголовок на странице с компьютерами")
    def get_desktops_title(self):
        return self.get_element(self.DESKTOPS_CONTENT_TITLE)

    @allure.step("Ищем заголовок на странице с ноутбуками")
    def get_laptops_and_notebooks_title(self):
        return self.get_element(self.LAPTOPS_AND_NOTEBOOKS_CONTENT_TITLE)

    @allure.step("Ищем заголовок на странице с компонентами")
    def get_components_title(self):
        return self.get_element(self.COMPONENTS_CONTENT_TITLE)

    @allure.step("Ищем заголовок на странице с планшетами")
    def get_tablets_title(self):
        return self.get_element(self.TABLETS_CONTENT_TITLE)

    @allure.step("Ищем заголовок на странице с программным обеспечением")
    def get_software_title(self):
        return self.get_element(self.SOFTWARE_CONTENT_TITLE)
