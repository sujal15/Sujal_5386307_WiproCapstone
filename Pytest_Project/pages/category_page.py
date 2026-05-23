from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger

class CategoryPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def verify_page_loaded(self):

        self.wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "product-base")
            )
        )

        assert "myntra" in self.driver.current_url.lower()

    def verify_products_visible(self):
        logger.info("Verifying products are displayed")
        products = self.driver.find_elements(
            By.CLASS_NAME,
            "product-base"
        )
        logger.info("Products loaded successfully")
        assert len(products) > 0

    def open_first_product(self):
        logger.info("Opening first product")
        products = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "product-base")
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            products[0]
        )
        logger.info("First product clicked")
        products[0].click()