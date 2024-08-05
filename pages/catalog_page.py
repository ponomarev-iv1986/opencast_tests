from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CatalogPage(BasePage):
    DESKTOPS_CONTENT_TITLE = (
        By.XPATH,
        "//div[@id='content']/h2[contains(text(), 'Desktops')]",
    )
    LAPTOPS_AND_NOTEBOOKS_CONTENT_TITLE = (
        By.XPATH,
        "//div[@id='content']/h2[contains(text(), 'Laptops & Notebooks')]",
    )
    COMPONENTS_CONTENT_TITLE = (
        By.XPATH,
        "//div[@id='content']/h2[contains(text(), 'Components')]",
    )
    TABLETS_CONTENT_TITLE = (
        By.XPATH,
        "//div[@id='content']/h2[contains(text(), 'Tablets')]",
    )
    SOFTWARE_CONTENT_TITLE = (
        By.XPATH,
        "//div[@id='content']/h2[contains(text(), 'Software')]",
    )

    def open_desktops_page(self):
        self.browser.get(self.browser.url + "/en-gb/catalog/desktops")

    def open_laptops_and_notebooks_page(self):
        self.browser.get(self.browser.url + "/en-gb/catalog/laptop-notebook")

    def open_components_page(self):
        self.browser.get(self.browser.url + "/en-gb/catalog/component")

    def open_tablets_page(self):
        self.browser.get(self.browser.url + "/en-gb/catalog/tablet")

    def open_software_page(self):
        self.browser.get(self.browser.url + "/en-gb/catalog/software")

    # GETTERS
    def get_desktops_title(self):
        return self.get_element(self.DESKTOPS_CONTENT_TITLE)

    def get_laptops_and_notebooks_title(self):
        return self.get_element(self.LAPTOPS_AND_NOTEBOOKS_CONTENT_TITLE)

    def get_components_title(self):
        return self.get_element(self.COMPONENTS_CONTENT_TITLE)

    def get_tablets_title(self):
        return self.get_element(self.TABLETS_CONTENT_TITLE)

    def get_software_title(self):
        return self.get_element(self.SOFTWARE_CONTENT_TITLE)
