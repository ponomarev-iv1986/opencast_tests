import os

import dotenv
import pytest
from selenium import webdriver

from pages.admin_page import AdminPage


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="http://127.0.0.1:8080")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    url = request.config.getoption("--url")

    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError('Поддерживаются только браузеры "chrome" и "firefox"')

    driver.maximize_window()
    driver.url = url

    yield driver

    driver.quit()


@pytest.fixture()
def login_admin_page(browser):
    dotenv.load_dotenv()
    admin_page = AdminPage(browser)
    admin_page.open_admin_page()
    admin_page.fill_username(os.getenv("LOGIN"))
    admin_page.fill_password(os.getenv("PASSWORD"))
    admin_page.submit()

    return admin_page
