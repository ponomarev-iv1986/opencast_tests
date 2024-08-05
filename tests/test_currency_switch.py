import allure
from allure_commons.types import Severity

from pages.home_page import HomePage


@allure.title("Проверка переключения валют")
@allure.severity(Severity.CRITICAL)
@allure.tag("TEST", "REGRESS")
@allure.label("owner", "IV_Ponomarev")
@allure.suite("Home page")
@allure.parent_suite("Opencart")
def test_currency_switch(browser):
    home_page = HomePage(browser)
    home_page.open_home_page()
    home_page.click_on_currency_switch()
    home_page.select_currency_value_by_index(0)
    home_page.currency_is("€")
    home_page.click_on_currency_switch()
    home_page.select_currency_value_by_index(1)
    home_page.currency_is("£")
    home_page.click_on_currency_switch()
    home_page.select_currency_value_by_index(2)
    home_page.currency_is("$")
