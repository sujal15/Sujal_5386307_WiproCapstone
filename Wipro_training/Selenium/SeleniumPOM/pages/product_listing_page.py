from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductListingPage:
    PRODUCT_TITLE = (By.CSS_SELECTOR, "a h2 span")
    BRAND_FILTER = (By.XPATH, "//span[contains(text(),'Logitech')]")
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_product_title(self):
        first_product = self.wait.until(
            EC.visibility_of_element_located(self.PRODUCT_TITLE)
        )
        print("\nFirst Product:", first_product.text)

    def all_products(self):
        product_titles = self.driver.find_elements(*self.PRODUCT_TITLE)

        print(f"\nFound {len(product_titles)} product titles on page one.\n")

        for i, title in enumerate(product_titles[:5], start=1):
            print(f"{i}. {title.text}")

        return len(product_titles) > 0

    from selenium.webdriver.support import expected_conditions as EC

    def select_brand_filter(self):
        # Wait until the filter is clickable
        brand_filter = self.wait.until(
            EC.element_to_be_clickable(self.BRAND_FILTER)
        )
        brand_filter.click()

    def check_product_titles_for_brand_filter(self, brandname):
        product_titles = self.wait.until(EC.visibility_of_all_elements_located(self.PRODUCT_TITLE))  # get all elements
        for title in product_titles:
            if brandname not in title.text:  # replace __contains__ with 'in'
                return False
        return True