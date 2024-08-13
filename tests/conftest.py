import json
import os

import allure
import dotenv
import pytest
from selenium import webdriver

from pages.admin_page import AdminPage


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="http://127.0.0.1:8080")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome != "passed":
        item.status = "failed"
    else:
        item.status = "passed"


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

    allure.attach(
        name=driver.session_id,
        body=json.dumps(driver.capabilities, indent=4, ensure_ascii=False),
        attachment_type=allure.attachment_type.JSON,
    )

    driver.maximize_window()
    driver.url = url

    yield driver

    if request.node.status == "failed":
        allure.attach(
            name="failure_screenshot",
            body=driver.get_screenshot_as_png(),
            attachment_type=allure.attachment_type.PNG,
        )
        allure.attach(
            name="page_source",
            body=driver.page_source,
            attachment_type=allure.attachment_type.HTML,
        )

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
