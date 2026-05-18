"""
Base Page Object
Provides common Selenium utilities inherited by all page classes.
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import logging

logger = logging.getLogger(__name__)


class BasePage:
    DEFAULT_TIMEOUT = 15

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.DEFAULT_TIMEOUT)

    # ── Waits ──────────────────────────────────────────────────────────────

    def wait_for_element(self, locator, timeout=None):
        t = timeout or self.DEFAULT_TIMEOUT
        return WebDriverWait(self.driver, t).until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_clickable(self, locator, timeout=None):
        t = timeout or self.DEFAULT_TIMEOUT
        return WebDriverWait(self.driver, t).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_visible(self, locator, timeout=None):
        t = timeout or self.DEFAULT_TIMEOUT
        return WebDriverWait(self.driver, t).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_text_in_element(self, locator, text, timeout=None):
        t = timeout or self.DEFAULT_TIMEOUT
        return WebDriverWait(self.driver, t).until(
            EC.text_to_be_present_in_element(locator, text)
        )

    # ── Actions ────────────────────────────────────────────────────────────

    def click(self, locator):
        element = self.wait_for_clickable(locator)
        element.click()
        logger.info(f"Clicked element: {locator}")

    def type_text(self, locator, text):
        element = self.wait_for_visible(locator)
        element.clear()
        element.send_keys(text)
        logger.info(f"Typed '{text}' into {locator}")

    def get_text(self, locator):
        element = self.wait_for_visible(locator)
        return element.text.strip()

    def is_element_present(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def is_element_enabled(self, locator):
        try:
            el = self.wait_for_element(locator, timeout=5)
            return el.is_enabled()
        except TimeoutException:
            return False

    def is_element_displayed(self, locator, timeout=5):
        try:
            el = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return el.is_displayed()
        except TimeoutException:
            return False

    def get_elements(self, locator):
        self.wait_for_element(locator)
        return self.driver.find_elements(*locator)

    def scroll_into_view(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def get_current_url(self):
        return self.driver.current_url

    def get_page_title(self):
        return self.driver.title
