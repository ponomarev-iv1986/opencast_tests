import allure
from allure_commons.types import Severity

from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.shopping_cart_page import ShoppingCartPage


@allure.title("Проверка добавления товара в корзину")
@allure.severity(Severity.CRITICAL)
@allure.tag("TEST", "REGRESS")
@allure.label("owner", "IV_Ponomarev")
@allure.suite("Shopping cart")
@allure.parent_suite("Opencart")
def test_add_to_shopping_cart(browser):
    home_page = HomePage(browser)
    shopping_cart_page = ShoppingCartPage(browser)
    product_page = ProductPage(browser)
    home_page.open_home_page()
    home_page.click_on_product("MacBook")
    product_page.add_to_shopping_cart()
    shopping_cart_page.open_shopping_cart_page()
    shopping_cart_page.have_product("MacBook")
