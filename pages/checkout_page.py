"""
Bag Page & Checkout Page Objects
Handles bag product verification, coupon entry, and checkout flow.
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import logging
import re

logger = logging.getLogger(__name__)


class BagPage(BasePage):
    # Bag items
    BAG_ITEM            = (By.CSS_SELECTOR, "div.bag-itemContainer, div[class*='bagItem']")
    BAG_PRODUCT_NAME    = (By.CSS_SELECTOR, "div.item-productDetail a, p[class*='productName']")
    BAG_PRODUCT_PRICE   = (By.CSS_SELECTOR, "span.bag-itemPrice strong, div[class*='itemPrice']")
    EMPTY_BAG_MSG       = (By.CSS_SELECTOR, "div[class*='emptyBag'], div[class*='empty-bag']")

    # Proceed
    PLACE_ORDER_BTN     = (By.CSS_SELECTOR, "div.bag-ghButton button, button[class*='placeOrder']")
    PROCEED_BTN         = (By.CSS_SELECTOR, "div.bag-ghButton, button[class*='proceed']")

    def is_bag_page_loaded(self):
        return (
            self.is_element_present(self.BAG_ITEM, timeout=10)
            or self.is_element_present(self.EMPTY_BAG_MSG, timeout=5)
        )

    def get_bag_items(self):
        return self.get_elements(self.BAG_ITEM)

    def get_bag_item_count(self):
        return len(self.get_bag_items())

    def get_first_item_name(self):
        return self.get_text(self.BAG_PRODUCT_NAME)

    def get_first_item_price(self):
        return self.get_text(self.BAG_PRODUCT_PRICE)

    def proceed_to_checkout(self):
        self.click(self.PLACE_ORDER_BTN)
        logger.info("Clicked Proceed / Place Order")


class CheckoutPage(BasePage):
    # Order summary
    ORDER_SUMMARY       = (By.CSS_SELECTOR, "div.order-summary, div[class*='orderSummary']")
    ORDER_ITEM_NAME     = (By.CSS_SELECTOR, "div[class*='itemName'], p[class*='productName']")
    ORDER_TOTAL         = (By.CSS_SELECTOR, "div.order-total span, span[class*='totalPrice'], div[class*='total'] strong")
    ORDER_ITEMS_SECTION = (By.CSS_SELECTOR, "div.checkout-order, div[class*='checkout']")

    # Coupon
    COUPON_INPUT        = (By.CSS_SELECTOR, "input[placeholder*='coupon'], input[placeholder*='Enter'], input[class*='coupon']")
    APPLY_COUPON_BTN    = (By.CSS_SELECTOR, "button[class*='applyCoupon'], span[class*='apply'], button[class*='apply']")
    COUPON_ERROR_MSG    = (By.CSS_SELECTOR, "div[class*='couponError'], p[class*='error'], span[class*='invalid']")
    COUPON_SUCCESS_MSG  = (By.CSS_SELECTOR, "div[class*='couponSuccess'], span[class*='saved']")

    # Login redirect
    LOGIN_FORM          = (By.CSS_SELECTOR, "div.login-container, form[class*='login'], input[type='tel']")

    def is_checkout_loaded(self):
        return self.is_element_present(self.ORDER_SUMMARY, timeout=10)

    def is_login_redirect(self):
        return self.is_element_present(self.LOGIN_FORM, timeout=5)

    def get_order_total(self):
        text = self.get_text(self.ORDER_TOTAL)
        numbers = re.findall(r'[\d,]+', text.replace('₹', ''))
        if numbers:
            return int(numbers[0].replace(',', ''))
        return 0

    def get_item_name_in_order(self):
        if self.is_element_present(self.ORDER_ITEM_NAME, timeout=5):
            return self.get_text(self.ORDER_ITEM_NAME)
        return ""

    def apply_coupon(self, code):
        self.type_text(self.COUPON_INPUT, code)
        self.click(self.APPLY_COUPON_BTN)
        logger.info(f"Applied coupon code: {code}")

    def is_coupon_error_shown(self):
        return self.is_element_present(self.COUPON_ERROR_MSG, timeout=5)

    def is_coupon_success_shown(self):
        return self.is_element_present(self.COUPON_SUCCESS_MSG, timeout=5)
