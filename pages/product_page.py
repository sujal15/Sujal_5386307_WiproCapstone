from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    FIRST_PRODUCT_CARD = (By.XPATH, "(//li[@class='product-base'])[1]")
    PRODUCT_NAME_HEADER = (By.XPATH, "//h1[@class='pdp-title']")
    SIZE_OPTIONS = (By.XPATH, "//button[contains(@class, 'size-buttons-size-button') and not(contains(@class, 'disabled'))]")
    ADD_TO_BAG_BTN = (By.XPATH, "//div[contains(text(), 'ADD TO BAG')]")
    GO_TO_BAG_BTN = (By.XPATH, "//span[contains(text(), 'Bag')]/parent::a")
    SIZE_ERROR_BUBBLE = (By.XPATH, "//span[contains(@class, 'size-buttons-select-size-error')]")
    NO_PRODUCTS_ERROR = (By.XPATH, "//h1[contains(text(), 'Could not find any matches') or contains(@class, 'title')]")

    def select_first_product(self):
        self.click(self.FIRST_PRODUCT_CARD)
        window_handles = self.driver.window_handles
        if len(window_handles) > 1:
            self.driver.switch_to.window(window_handles[1])

    def choose_available_size(self):
        if self.is_element_present(self.SIZE_OPTIONS):
            self.click(self.SIZE_OPTIONS)

    def click_add_to_bag(self):
        self.click(self.ADD_TO_BAG_BTN)

    def go_to_checkout_bag(self):
        self.click(self.GO_TO_BAG_BTN)