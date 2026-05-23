
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductListingPage:
    PRODUCT_TITLES = (By.CSS_SELECTOR, "a h2 span")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_product_title(self):
        first_product = self.wait.until(EC.visibility_of_element_located(self.PRODUCT_TITLES))
        print("\nFirst product: ", first_product.text)

    def all_products(self):
        product_titles = self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_TITLES))
        print(f"\nFound {len(product_titles)} product titles on page one.\n")

        for i, title in enumerate(product_titles[:5], start=1):
            print(f"{i}. {title.text}")

        return len(product_titles) > 0

    def brand_filter_locator(self, brandname):
        return (By.XPATH, f"//span[text()='{brandname}']/parent::a/descendant::i")

    def select_brand_filter(self, brandname):
        brand_filter = self.driver.find_element(*self.brand_filter_locator(brandname))
        brand_filter.click()
        self.wait_for_products_to_load()

    def wait_for_products_to_load(self):
        self.wait.until(EC.visibility_of_element_located(self.PRODUCT_TITLES))
        time.sleep(1)

    def check_product_titles_for_brand_filter(self, brandname):
        product_titles = self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_TITLES))

        for title in product_titles:
            print("Title: ", title.text)
            time.sleep(1)

        return True

    def mensize_locator(self, mensize):
        return (By.XPATH, f"(//span[@class='a-list-item']/descendant::button[@value='{mensize}'])[1]")

    def select_mensize_filter(self, mensize):
        mensize_filter = self.driver.find_element(*self.mensize_locator(mensize))
        mensize_filter.click()
        self.wait_for_products_to_load()

    def check_size_in_title(self, mensize):
        return mensize in self.driver.title