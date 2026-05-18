"""
Home Page & GENZ Section Page Objects
Handles navigation from Myntra homepage into the GENZ section.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
import logging

logger = logging.getLogger(__name__)


class HomePage(BasePage):
    # Locators
    LOGO              = (By.CSS_SELECTOR, "a.desktop-logo")
    SEARCH_BAR        = (By.CSS_SELECTOR, "input.desktop-searchBar")
    PROFILE_ICON      = (By.CSS_SELECTOR, "a[href='/login']")
    BAG_ICON          = (By.CSS_SELECTOR, "a[href='/checkout/bag']")
    BAG_COUNT         = (By.CSS_SELECTOR, "span.bagItemsCount")
    NAV_ITEMS         = (By.CSS_SELECTOR, "nav.desktop-navbar a")
    GENZ_NAV_LINK     = (By.XPATH, "//nav//a[contains(translate(text(),'GENZ','genz'),'genz')]")

    def open(self, url):
        self.driver.get(url)
        self.wait_for_element(self.LOGO)
        logger.info(f"Opened Myntra: {url}")

    def navigate_to_genz(self):
        genz_link = self.wait_for_clickable(self.GENZ_NAV_LINK)
        genz_link.click()
        logger.info("Navigated to GENZ section")

    def get_bag_count(self):
        if self.is_element_present(self.BAG_COUNT, timeout=3):
            return int(self.get_text(self.BAG_COUNT))
        return 0

    def go_to_bag(self):
        self.click(self.BAG_ICON)
        logger.info("Clicked bag icon")


class GenzPage(BasePage):
    # Locators — category tiles on GENZ landing
    CATEGORY_TILE         = (By.CSS_SELECTOR, "div.genz-category-tile, div[class*='category']")
    CATEGORY_LINK         = lambda self, name: (
        By.XPATH,
        f"//a[contains(translate(normalize-space(.),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'{name.lower()}')]"
    )

    def select_category(self, category_name):
        locator = self.CATEGORY_LINK(category_name)
        element = self.wait_for_clickable(locator)
        ActionChains(self.driver).move_to_element(element).click().perform()
        logger.info(f"Selected category: {category_name}")

    def hover_and_select_subcategory(self, category_name, subcategory_name):
        cat_locator = self.CATEGORY_LINK(category_name)
        cat_element = self.wait_for_element(cat_locator)
        ActionChains(self.driver).move_to_element(cat_element).perform()

        sub_locator = self.CATEGORY_LINK(subcategory_name)
        sub_element = self.wait_for_clickable(sub_locator)
        sub_element.click()
        logger.info(f"Selected: {category_name} → {subcategory_name}")
