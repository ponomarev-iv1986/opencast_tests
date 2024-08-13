import json
import os

import allure
import dotenv
import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions

from pages.admin_page import AdminPage


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="http://192.168.3.107:8081")
    parser.addoption("--remote", action="store_true")
    parser.addoption("--executor", action="store", default="127.0.0.1")
    parser.addoption("--bv", action="store", default="127.0")
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--video", action="store_true")


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
    remote = request.config.getoption("--remote")
    executor = request.config.getoption("--executor")
    browser_version = request.config.getoption("--bv")
    vnc = request.config.getoption("--vnc")
    video = request.config.getoption("--video")

    if remote:
        executor_url = f"http://{executor}:4444/wd/hub"
        if browser_name == "chrome":
            options = ChromeOptions()
        elif browser_name == "firefox":
            options = FirefoxOptions()
        else:
            raise ValueError('Поддерживаются только браузеры "chrome" и "firefox"')
        capabilities = {
            "browserName": browser_name,
            "browserVersion": browser_version,
            "selenoid:options": {
                "enableVNC": vnc,
                "name": request.node.name,
                "screenResolution": "1920x1080",
                "enableVideo": video,
                "timeZone": "Europe/Moscow",
                "env": ["LANG=ru_RU.UTF-8", "LANGUAGE=ru:en", "LC_ALL=ru_RU.UTF-8"],
            },
            "acceptInsecureCerts": True,
        }
        options.capabilities.update(capabilities)
        driver = webdriver.Remote(
            command_executor=executor_url,
            options=options,
        )
    else:
        if browser_name == "chrome":
            driver = webdriver.Chrome()
        elif browser_name == "firefox":
            driver = webdriver.Firefox()
        else:
            raise ValueError('Поддерживаются только браузеры "chrome" и "firefox"')
        driver.maximize_window()

    allure.attach(
        name=driver.session_id,
        body=json.dumps(driver.capabilities, indent=4, ensure_ascii=False),
        attachment_type=allure.attachment_type.JSON,
    )

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
