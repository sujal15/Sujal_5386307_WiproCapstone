from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    SEARCH_BAR = (By.XPATH, "//input[contains(@class, 'desktop-searchBar')]")
    SEARCH_ICON = (By.XPATH, "//a[contains(@class, 'desktop-submit')]")

    def search_genz_category(self, query):
        self.send_keys(self.SEARCH_BAR, f"GenZ {query}")
        self.click(self.SEARCH_ICON)