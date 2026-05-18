import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click(self, locator):
        logging.info(f"Interacting Click on Element Selector: {locator}")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, text):
        logging.info(f"Injecting text input string value '{text}' into Field: {locator}")
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def is_element_present(self, locator):
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except Exception:
            return False

    def close_tabs_except_root(self):
        handles = self.driver.window_handles
        while len(handles) > 1:
            self.driver.switch_to.window(handles[-1])
            self.driver.close()
            handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])