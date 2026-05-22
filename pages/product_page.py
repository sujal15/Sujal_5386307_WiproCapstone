from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ProductPage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def switch_to_product_tab(self):

        self.wait.until(
            lambda d: len(d.window_handles) > 1
        )

        self.driver.switch_to.window(
            self.driver.window_handles[-1]
        )

        print("Switched to product tab")

    def select_size(self):

        time.sleep(3)

        sizes = self.driver.find_elements(
            By.XPATH,
            "//p[contains(@class,'size-buttons-unified-size')]"
        )

        print("TOTAL SIZES FOUND:", len(sizes))

        if len(sizes) == 0:
            raise Exception("No sizes available")

        selected = False

        for size in sizes:

            try:

                text = size.text.strip()

                print("SIZE:", text)

                if size.is_displayed() and size.is_enabled():

                    self.driver.execute_script(
                        "arguments[0].click();",
                        size
                    )

                    print("Size selected:", text)

                    selected = True
                    break

            except Exception as e:
                print("Unable to click size:", e)

        if not selected:
            raise Exception("Could not select any size")

    def add_to_bag(self):

        time.sleep(3)

        buttons = self.driver.find_elements(
            By.XPATH,
            "//*[contains(text(),'ADD TO BAG')]"
        )

        print("ADD TO BAG BUTTONS FOUND:", len(buttons))

        if len(buttons) == 0:
            raise Exception("ADD TO BAG button not found")

        clicked = False

        for btn in buttons:

            try:

                if btn.is_displayed():

                    self.driver.execute_script(
                        "arguments[0].click();",
                        btn
                    )

                    print("ADD TO BAG clicked")

                    clicked = True
                    break

            except Exception as e:
                print("Button click failed:", e)

        if not clicked:
            raise Exception("Unable to click ADD TO BAG")

    def verify_add_to_bag(self):

        time.sleep(5)

        page = self.driver.page_source.lower()

        if "go to bag" in page:
            print("Product added successfully")
            assert True

        elif "added to bag" in page:
            print("Product added successfully")
            assert True

        else:
            raise Exception("Product was NOT added to bag")



    def open_bag(self):

        wait = WebDriverWait(self.driver, 20)

        bag = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//span[text()='Bag']/parent::*"
                )
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            bag
        )

        print("Opened Shopping Bag")

    def verify_item_in_bag(self):

        wait = WebDriverWait(self.driver, 20)

        item = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[contains(@class,'itemContainer-base-brand')]"
                )
            )
        )

        print(
            "Item present:",
            item.text
        )

        assert item.is_displayed(), \
            "No item found in shopping bag"

    def click_place_order(self):

        wait = WebDriverWait(self.driver, 20)

        place = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[text()='PLACE ORDER']"
                )
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            place
        )

        print(
            "Clicked Place Order"
        )