import allure
from allure_commons.types import Severity

from pages.admin_page import AdminPage
from pages.catalog_page import CatalogPage
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from pages.shopping_cart_page import ShoppingCartPage


@allure.title("Проверка элементов главной страницы")
@allure.severity(Severity.NORMAL)
@allure.tag("TEST", "REGRESS")
@allure.label("owner", "IV_Ponomarev")
@allure.suite("Home page")
@allure.parent_suite("Opencart")
def test_homepage(browser):
    home_page = HomePage(browser)
    home_page.open_home_page()
    home_page.get_opencart_image()
    home_page.get_menu()
    home_page.get_carousel_banner_0()
    home_page.get_products()
    home_page.get_carousel_banner_1()


@allure.title("Проверка элементов каталога")
@allure.severity(Severity.NORMAL)
@allure.tag("TEST", "REGRESS")
@allure.label("owner", "IV_Ponomarev")
@allure.suite("Catalog")
@allure.parent_suite("Opencart")
def test_catalog(browser):
    catalog = CatalogPage(browser)
    catalog.open_desktops_page()
    catalog.get_desktops_title()

    catalog.open_laptops_and_notebooks_page()
    catalog.get_laptops_and_notebooks_title()

    catalog.open_components_page()
    catalog.get_components_title()

    catalog.open_tablets_page()
    catalog.get_tablets_title()

    catalog.open_software_page()
    catalog.get_software_title()


@allure.title("Проверка элементов корзины")
@allure.severity(Severity.NORMAL)
@allure.tag("TEST", "REGRESS")
@allure.label("owner", "IV_Ponomarev")
@allure.suite("Shopping cart")
@allure.parent_suite("Opencart")
def test_shopping_cart(browser):
    shopping_cart_page = ShoppingCartPage(browser)
    shopping_cart_page.open_shopping_cart_page()
    shopping_cart_page.get_opencart_image()
    shopping_cart_page.get_menu()
    shopping_cart_page.get_shopping_cart_title()
    shopping_cart_page.get_empty_shopping_cart_title()
    shopping_cart_page.get_continue_button()


@allure.title("Проверка элементов страницы администрирования")
@allure.severity(Severity.NORMAL)
@allure.tag("TEST", "REGRESS")
@allure.label("owner", "IV_Ponomarev")
@allure.suite("Administration page")
@allure.parent_suite("Opencart")
def test_administration_page(browser):
    admin_page = AdminPage(browser)
    admin_page.open_admin_page()
    admin_page.get_opencart_image()
    admin_page.get_login_form()
    admin_page.get_username_input()
    admin_page.get_password_input()
    admin_page.get_submit_button()


@allure.title("Проверка элементов страницы регистрации")
@allure.severity(Severity.NORMAL)
@allure.tag("TEST", "REGRESS")
@allure.label("owner", "IV_Ponomarev")
@allure.suite("Registration page")
@allure.parent_suite("Opencart")
def test_registration_page(browser):
    registration_page = RegistrationPage(browser)
    registration_page.open_registration_page()
    registration_page.get_first_name_input()
    registration_page.get_last_name_input()
    registration_page.get_email_input()
    registration_page.get_password_input()
    registration_page.get_submit_button()
