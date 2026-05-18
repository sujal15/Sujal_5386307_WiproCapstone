"""
Product Listing Page Object
Handles filter application, sort, and product card interactions.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
import logging
import re

logger = logging.getLogger(__name__)


class ProductListingPage(BasePage):
    # Page identity
    PAGE_TITLE          = (By.CSS_SELECTOR, "h1.title-title, div.listing-pageTitle, h1")

    # Product cards
    PRODUCT_CARDS       = (By.CSS_SELECTOR, "li.product-base, div.product-base")
    PRODUCT_COUNT_TEXT  = (By.CSS_SELECTOR, "span.title-count, div.results-count, span[class*='count']")
    FIRST_PRODUCT       = (By.CSS_SELECTOR, "li.product-base:first-child, div.product-base:first-child")

    # Filters sidebar
    FILTER_SECTION      = (By.CSS_SELECTOR, "div.filter-base-container, div[class*='filter']")
    FILTER_HEADER       = lambda self, name: (
        By.XPATH,
        f"//div[contains(@class,'filter') and .//span[contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'{name.lower()}')]]"
    )
    FILTER_OPTION       = lambda self, value: (
        By.XPATH,
        f"//div[contains(@class,'filter')]//label[contains(translate(normalize-space(.),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'{value.lower()}')]"
    )
    PRICE_MIN_INPUT     = (By.CSS_SELECTOR, "input.priceInputBox:first-of-type, input[placeholder*='Min']")
    PRICE_MAX_INPUT     = (By.CSS_SELECTOR, "input.priceInputBox:last-of-type, input[placeholder*='Max']")
    APPLY_FILTER_BTN    = (By.CSS_SELECTOR, "button.priceInputApply, button[class*='apply']")
    APPLIED_FILTERS     = (By.CSS_SELECTOR, "div.applied-filters span, div[class*='applied'] span")

    # Sort
    SORT_DROPDOWN       = (By.CSS_SELECTOR, "div.sort-sortBy, button[class*='sort']")
    SORT_OPTION         = lambda self, label: (
        By.XPATH,
        f"//li[contains(translate(normalize-space(.),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'{label.lower()}')]"
    )

    # No results
    NO_RESULTS_MSG      = (By.CSS_SELECTOR, "div.no-results, div[class*='noResults'], div[class*='empty']")

    def is_listing_page_loaded(self):
        return self.is_element_present(self.PRODUCT_CARDS, timeout=10)

    def get_product_count(self):
        if self.is_element_present(self.PRODUCT_COUNT_TEXT, timeout=5):
            text = self.get_text(self.PRODUCT_COUNT_TEXT)
            numbers = re.findall(r'\d+', text.replace(',', ''))
            return int(numbers[0]) if numbers else 0
        cards = self.get_elements(self.PRODUCT_CARDS)
        return len(cards)

    def get_visible_product_cards(self):
        return self.get_elements(self.PRODUCT_CARDS)

    def apply_filter(self, filter_name, value):
        header_locator = self.FILTER_HEADER(filter_name)
        if self.is_element_present(header_locator, timeout=5):
            self.scroll_into_view(header_locator)
            self.click(header_locator)

        option_locator = self.FILTER_OPTION(value)
        self.click(option_locator)
        logger.info(f"Applied filter '{filter_name}' = '{value}'")
        self._wait_for_listing_refresh()

    def apply_price_filter(self, min_price, max_price):
        self.type_text(self.PRICE_MIN_INPUT, str(min_price))
        self.type_text(self.PRICE_MAX_INPUT, str(max_price))
        if self.is_element_present(self.APPLY_FILTER_BTN, timeout=3):
            self.click(self.APPLY_FILTER_BTN)
        logger.info(f"Applied price filter: ₹{min_price} – ₹{max_price}")
        self._wait_for_listing_refresh()

    def sort_by(self, label):
        self.click(self.SORT_DROPDOWN)
        self.click(self.SORT_OPTION(label))
        logger.info(f"Sorted by: {label}")
        self._wait_for_listing_refresh()

    def click_first_product(self):
        cards = self.get_visible_product_cards()
        if not cards:
            raise AssertionError("No product cards found on the listing page")
        cards[0].click()
        logger.info("Clicked first product card")

    def is_no_results_shown(self):
        return self.is_element_present(self.NO_RESULTS_MSG, timeout=5)

    def _wait_for_listing_refresh(self):
        import time
        time.sleep(1.5)
        self.wait_for_element(self.PRODUCT_CARDS, timeout=15)
