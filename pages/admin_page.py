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

    def open_admin_page(self):
        self.browser.get(self.browser.url + "/administration")

    # GETTERS
    def get_opencart_image(self):
        return self.get_element(self.OPENCART_IMAGE)

    def get_login_form(self):
        return self.get_element(self.LOGIN_FORM)

    def get_username_input(self):
        return self.get_element(self.USERNAME_INPUT)

    def get_password_input(self):
        return self.get_element(self.PASSWORD_INPUT)

    def get_submit_button(self):
        return self.get_element(self.SUBMIT_BUTTON)

    def get_profile_name(self):
        return self.get_element(self.PROFILE_NAME)

    def get_menu_catalog(self):
        return self.get_element(self.MENU_CATALOG)

    def get_menu_catalog_products(self):
        return self.get_element(self.MENU_CATALOG_PRODUCTS)

    def get_add_product_button(self):
        return self.get_element(self.ADD_PRODUCT_BUTTON)

    def get_product_name_input(self):
        return self.get_element(self.PRODUCT_NAME_INPUT)

    def get_meta_title_tag_input(self):
        return self.get_element(self.META_TAG_TITLE_INPUT)

    def get_data_navigation_link(self):
        return self.get_elements(self.NAV_TABS_PANEL)[1]

    def get_model_input(self):
        return self.get_element(self.MODEL_INPUT)

    def get_ceo_navigation_link(self):
        return self.get_elements(self.NAV_TABS_PANEL)[10]

    def get_keyword_input(self):
        return self.get_element(self.KEYWORD_INPUT)

    def get_save_product_button(self):
        return self.get_element(self.SAVE_PRODUCT_BUTTON)

    def get_first_product(self):
        return self.get_elements(self.PRODUCT_CHECKBOXES)[1]

    def get_delete_product_button(self):
        return self.get_element(self.DELETE_PRODUCT_BUTTON)

    # ACTIONS
    def fill_username(self, value: str):
        self.type(self.get_username_input(), value)

    def fill_password(self, value: str):
        self.type(self.get_password_input(), value)

    def submit(self):
        self.click(self.get_submit_button())

    def click_menu_catalog(self):
        self.click(self.get_menu_catalog())

    def click_catalog_products(self):
        self.click(self.get_menu_catalog_products())

    def click_add_product_button(self):
        self.click(self.get_add_product_button())

    def fill_product_name(self, value: str):
        self.type(self.get_product_name_input(), value)

    def fill_meta_tag_title_input(self, value: str):
        self.type(self.get_meta_title_tag_input(), value)

    def click_data_navigation_link(self):
        self.click(self.get_data_navigation_link())

    def fill_model_input(self, value: str):
        self.type(self.get_model_input(), value)

    def click_ceo_navigation_link(self):
        self.click(self.get_ceo_navigation_link())

    def fill_keyword_input(self, value: str):
        self.type(self.get_keyword_input(), value)

    def click_save_product_button(self):
        self.click(self.get_save_product_button())

    def click_first_product(self):
        self.click(self.get_first_product())

    def click_delete_product_button(self):
        self.click(self.get_delete_product_button())

    def accept_alert(self):
        self.get_alert().accept()
