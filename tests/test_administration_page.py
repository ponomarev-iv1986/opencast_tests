from faker import Faker


def test_add_product(login_admin_page):
    fake = Faker()
    login_admin_page.click_menu_catalog()
    login_admin_page.click_catalog_products()
    login_admin_page.click_add_product_button()
    login_admin_page.fill_product_name(f"Product{fake.numerify('######')}")
    login_admin_page.fill_meta_tag_title_input(f"Tag{fake.numerify('######')}")
    login_admin_page.click_data_navigation_link()
    login_admin_page.fill_model_input(f"Model{fake.numerify('######')}")
    login_admin_page.click_ceo_navigation_link()
    login_admin_page.fill_keyword_input(f"Keyword{fake.numerify('######')}")
    login_admin_page.click_save_product_button()
    login_admin_page.alert_element.have_text("Success: You have modified products!")


def test_remove_product(login_admin_page):
    login_admin_page.click_menu_catalog()
    login_admin_page.click_catalog_products()
    login_admin_page.click_first_product()
    login_admin_page.click_delete_product_button()
    login_admin_page.accept_alert()
    login_admin_page.alert_element.have_text("Success: You have modified products!")
