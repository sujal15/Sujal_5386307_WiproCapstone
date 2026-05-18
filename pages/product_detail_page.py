"""
Product Detail Page Object
Handles size selection, wishlist, Add to Bag, and size chart interactions.
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import logging

logger = logging.getLogger(__name__)


class ProductDetailPage(BasePage):
    # Product info
    PRODUCT_NAME        = (By.CSS_SELECTOR, "h1.pdp-name, h1[class*='name'], h1.title")
    PRODUCT_PRICE       = (By.CSS_SELECTOR, "span.pdp-price, div[class*='price'] strong, span.price-offer")
    PRODUCT_IMAGES      = (By.CSS_SELECTOR, "div.image-grid img, div.pdp-image img, img[class*='image']")
    BRAND_NAME          = (By.CSS_SELECTOR, "h1.pdp-title, div.pdp-brand")

    # Size selection
    SIZE_CONTAINER      = (By.CSS_SELECTOR, "div.size-buttons-container, div[class*='size']")
    SIZE_OPTION         = lambda self, size: (
        By.XPATH,
        f"//div[contains(@class,'size')]//button[contains(normalize-space(text()),'{size}')] | "
        f"//div[contains(@class,'size')]//label[contains(normalize-space(text()),'{size}')]"
    )
    AVAILABLE_SIZES     = (By.CSS_SELECTOR, "button.size-buttons-buttonContainer:not(.size-buttons-buttonContainer-soldOut)")
    UNAVAILABLE_SIZE_CLS = "size-buttons-buttonContainer-soldOut"

    # Size chart
    SIZE_CHART_LINK     = (By.CSS_SELECTOR, "a[class*='sizeChart'], button[class*='sizeChart'], a[data-component='SIZE_CHART']")
    SIZE_CHART_POPUP    = (By.CSS_SELECTOR, "div.size-chart-container, div[class*='sizeChart']")
    SIZE_CHART_TABLE    = (By.CSS_SELECTOR, "table.sizeChartTable, table[class*='size']")

    # Actions
    ADD_TO_BAG_BTN      = (By.CSS_SELECTOR, "div.pdp-add-to-bag button, button.btn-addToBag, div[class*='addToBag'] button")
    MOVE_TO_WISHLIST    = (By.CSS_SELECTOR, "div.pdp-wishlist, button[class*='wishlist']")
    WISHLIST_HEART      = (By.CSS_SELECTOR, "button.pdp-wishlistIcon, div[class*='wishlist'] button, i[class*='wishlist']")
    WISHLIST_ACTIVE_CLS = "pdp-wishlistIcon--wishlisted"
    OOS_TEXT            = (By.CSS_SELECTOR, "div[class*='outOfStock'], div[class*='soldOut'], p[class*='outOfStock']")
    NOTIFY_ME_BTN       = (By.CSS_SELECTOR, "button[class*='notify'], div[class*='notifyMe']")

    # Toast / success messages
    TOAST_MSG           = (By.CSS_SELECTOR, "div.toast, div[class*='toast'], div[class*='snackbar']")
    WISHLIST_SUCCESS    = (By.XPATH, "//div[contains(text(),'Wishlist') or contains(text(),'wishlist')]")

    def is_product_detail_loaded(self):
        return (
            self.is_element_present(self.PRODUCT_NAME, timeout=10)
            and self.is_element_present(self.PRODUCT_PRICE, timeout=5)
            and self.is_element_present(self.PRODUCT_IMAGES, timeout=5)
        )

    def get_product_name(self):
        return self.get_text(self.PRODUCT_NAME)

    def get_product_price(self):
        return self.get_text(self.PRODUCT_PRICE)

    def has_size_options(self):
        return self.is_element_present(self.SIZE_CONTAINER, timeout=5)

    def select_size(self, size):
        locator = self.SIZE_OPTION(size)
        self.click(locator)
        logger.info(f"Selected size: {size}")

    def select_first_available_size(self):
        sizes = self.get_elements(self.AVAILABLE_SIZES)
        if not sizes:
            raise AssertionError("No available sizes found on product page")
        sizes[0].click()
        logger.info("Selected first available size")
        return sizes[0].text.strip()

    def is_size_unavailable(self, size):
        locator = self.SIZE_OPTION(size)
        try:
            el = self.wait_for_element(locator, timeout=5)
            classes = el.get_attribute("class") or ""
            disabled = el.get_attribute("disabled")
            return self.UNAVAILABLE_SIZE_CLS in classes or disabled is not None
        except Exception:
            return False

    def click_add_to_bag(self):
        self.click(self.ADD_TO_BAG_BTN)
        logger.info("Clicked Add to Bag")

    def is_add_to_bag_disabled(self):
        try:
            el = self.wait_for_element(self.ADD_TO_BAG_BTN, timeout=5)
            disabled = el.get_attribute("disabled")
            classes = el.get_attribute("class") or ""
            return disabled is not None or "disabled" in classes
        except Exception:
            return True

    def click_wishlist(self):
        self.click(self.WISHLIST_HEART)
        logger.info("Clicked wishlist icon")

    def is_wishlist_active(self):
        try:
            el = self.wait_for_element(self.WISHLIST_HEART, timeout=5)
            return self.WISHLIST_ACTIVE_CLS in (el.get_attribute("class") or "")
        except Exception:
            return False

    def is_wishlist_success_shown(self):
        return (
            self.is_element_present(self.TOAST_MSG, timeout=5)
            or self.is_element_present(self.WISHLIST_SUCCESS, timeout=5)
        )

    def is_out_of_stock(self):
        return self.is_element_present(self.OOS_TEXT, timeout=5)

    def is_notify_me_shown(self):
        return self.is_element_present(self.NOTIFY_ME_BTN, timeout=5)

    def open_size_chart(self):
        self.click(self.SIZE_CHART_LINK)
        self.wait_for_visible(self.SIZE_CHART_POPUP)
        logger.info("Opened size chart popup")

    def is_size_chart_open(self):
        return self.is_element_present(self.SIZE_CHART_POPUP, timeout=5)
