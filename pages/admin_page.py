import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AdminPage(BasePage):
    OPENCART_IMAGE = By.CSS_SELECTOR, "img[title='OpenCart']"
    LOGIN_FORM = By.CSS_SELECTOR, ".card"
    USERNAME_INPUT = By.CSS_SELECTOR, "input[name=username]"
    PASSWORD_INPUT = By.CSS_SELECTOR, "input[name=password]"
    SUBMIT_BUTTON = By.CSS_SELECTOR, "button[type=submit]"
    PROFILE_NAME = By.XPATH, "//span[contains(text(), 'John Doe')]"
    MENU_CATALOG = By.CSS_SELECTOR, "#menu-catalog"
    MENU_CATALOG_PRODUCTS = By.XPATH, "//*[@id='menu-catalog']//*[text()='Products']"
    ADD_PRODUCT_BUTTON = By.CSS_SELECTOR, ".float-end .btn-primary"
    PRODUCT_NAME_INPUT = By.CSS_SELECTOR, "#input-name-1"
    META_TAG_TITLE_INPUT = By.CSS_SELECTOR, "#input-meta-title-1"
    MODEL_INPUT = By.CSS_SELECTOR, "#input-model"
    KEYWORD_INPUT = By.CSS_SELECTOR, "#input-keyword-0-1"
    NAV_TABS_PANEL = By.CSS_SELECTOR, "#form-product>.nav-tabs>li"
    SAVE_PRODUCT_BUTTON = By.CSS_SELECTOR, ".page-header .btn-primary"
    PRODUCT_CHECKBOXES = By.CSS_SELECTOR, ".form-check-input"
    DELETE_PRODUCT_BUTTON = By.CSS_SELECTOR, ".float-end .btn-danger"

    @allure.step("Открываем страницу администрирования")
    def open_admin_page(self):
        self.open("/administration")

    # GETTERS
    @allure.step("Ищем логотип")
    def get_opencart_image(self):
        return self.get_element(self.OPENCART_IMAGE)

    @allure.step("Ищем форму ввода имени и пароля")
    def get_login_form(self):
        return self.get_element(self.LOGIN_FORM)

    @allure.step("Ищем поле ввода имени")
    def get_username_input(self):
        return self.get_element(self.USERNAME_INPUT)

    @allure.step("Ищем поле ввода пароля")
    def get_password_input(self):
        return self.get_element(self.PASSWORD_INPUT)

    @allure.step("Ищем поле кнопку подтверждения")
    def get_submit_button(self):
        return self.get_element(self.SUBMIT_BUTTON)

    @allure.step("Ищем имя профиля")
    def get_profile_name(self):
        return self.get_element(self.PROFILE_NAME)

    @allure.step("Ищем ссылку 'Catalog'")
    def get_menu_catalog(self):
        return self.get_element(self.MENU_CATALOG)

    @allure.step("Ищем ссылку 'Products'")
    def get_menu_catalog_products(self):
        return self.get_element(self.MENU_CATALOG_PRODUCTS)

    @allure.step("Ищем кнопку добавления нового продукта")
    def get_add_product_button(self):
        return self.get_element(self.ADD_PRODUCT_BUTTON)

    @allure.step("Ищем поле ввода имени продукта")
    def get_product_name_input(self):
        return self.get_element(self.PRODUCT_NAME_INPUT)

    @allure.step("Ищем поле ввода мета тега продукта")
    def get_meta_title_tag_input(self):
        return self.get_element(self.META_TAG_TITLE_INPUT)

    @allure.step("Ищем ссылку 'Data' в панели навигции")
    def get_data_navigation_link(self):
        return self.get_elements(self.NAV_TABS_PANEL)[1]

    @allure.step("Ищем поле ввода модели продукта")
    def get_model_input(self):
        return self.get_element(self.MODEL_INPUT)

    @allure.step("Ищем ссылку 'SEO' в панели навигции")
    def get_ceo_navigation_link(self):
        return self.get_elements(self.NAV_TABS_PANEL)[10]

    @allure.step("Ищем поле ввода ключа продукта")
    def get_keyword_input(self):
        return self.get_element(self.KEYWORD_INPUT)

    @allure.step("Ищем кнопку сохранения продукта")
    def get_save_product_button(self):
        return self.get_element(self.SAVE_PRODUCT_BUTTON)

    @allure.step("Ищем чекбокс первого по счету продукта")
    def get_first_product(self):
        return self.get_elements(self.PRODUCT_CHECKBOXES)[1]

    @allure.step("Ищем кнопку удаления продукта")
    def get_delete_product_button(self):
        return self.get_element(self.DELETE_PRODUCT_BUTTON)

    # ACTIONS
    def fill_username(self, value: str):
        with allure.step("Вводим имя пользователя"):
            self.type(self.get_username_input(), value)

    def fill_password(self, value: str):
        with allure.step("Вводим пароль"):
            self.type(self.get_password_input(), value)

    @allure.step("Нажимаем кнопку подтверждения")
    def submit(self):
        self.click(self.get_submit_button())

    @allure.step("Нажимаем ссылку 'Catalog'")
    def click_menu_catalog(self):
        self.click(self.get_menu_catalog())

    @allure.step("Нажимаем ссылку 'Products'")
    def click_catalog_products(self):
        self.click(self.get_menu_catalog_products())

    @allure.step("Нажимаем кнопку добавления нового продукта")
    def click_add_product_button(self):
        self.click(self.get_add_product_button())

    @allure.step("Вводим имя продукта {value}")
    def fill_product_name(self, value: str):
        self.type(self.get_product_name_input(), value)

    @allure.step("Вводим мета тег продукта {value}")
    def fill_meta_tag_title_input(self, value: str):
        self.type(self.get_meta_title_tag_input(), value)

    @allure.step("Нажимаем ссылку 'Data'")
    def click_data_navigation_link(self):
        self.click(self.get_data_navigation_link())

    @allure.step("Вводим модель продукта {value}")
    def fill_model_input(self, value: str):
        self.type(self.get_model_input(), value)

    @allure.step("Нажимаем ссылку 'SEO'")
    def click_ceo_navigation_link(self):
        self.click(self.get_ceo_navigation_link())

    @allure.step("Вводим ключ продукта {value}")
    def fill_keyword_input(self, value: str):
        self.type(self.get_keyword_input(), value)

    @allure.step("Кнопку сохранения продукта")
    def click_save_product_button(self):
        self.click(self.get_save_product_button())

    @allure.step("Выбираем первый по списку продукт")
    def click_first_product(self):
        self.click(self.get_first_product())

    @allure.step("Нажимаем кнопку удаления продукта")
    def click_delete_product_button(self):
        self.click(self.get_delete_product_button())

    @allure.step("Подтверждаем alert")
    def accept_alert(self):
        self.get_alert().accept()
