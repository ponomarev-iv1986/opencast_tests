from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.shopping_cart_page import ShoppingCartPage


def test_add_to_shopping_cart(browser):
    home_page = HomePage(browser)
    shopping_cart_page = ShoppingCartPage(browser)
    product_page = ProductPage(browser)
    home_page.open_home_page()
    home_page.click_on_product("MacBook")
    product_page.add_to_shopping_cart()
    shopping_cart_page.open_shopping_cart_page()
    shopping_cart_page.have_product("MacBook")
