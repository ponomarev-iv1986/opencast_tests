import os

import dotenv

from pages.admin_page import AdminPage


def test_login_administration(browser):
    dotenv.load_dotenv()
    admin_page = AdminPage(browser)
    admin_page.open_admin_page()
    admin_page.fill_username(os.getenv("LOGIN"))
    admin_page.fill_password(os.getenv("PASSWORD"))
    admin_page.submit()
    admin_page.get_profile_name()
