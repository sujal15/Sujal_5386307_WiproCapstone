from pages.home_page import HomePage
from pages.category_page import CategoryPage
from pages.product_page import ProductPage
import time
import allure

from utils.logger import logger


class TestGENZCategories:

    #E2E TESTING
    @allure.feature("GENZ")
    @allure.story("Women's Dresses E2E")
    def test_womens_dresses_e2e(self, driver):

        home = HomePage(driver)
        category = CategoryPage(driver)
        product = ProductPage(driver)
        with allure.step("Open Myntra"):
            home.open_myntra()
        with allure.step("Hover GENZ"):
            home.hover_genz()
        with allure.step("Click Dresses"):
            home.click_women_dresses()

        category.verify_page_loaded()
        with allure.step("Verify products"):
            category.verify_products_visible()
        with allure.step("Open Product"):
            category.open_first_product()

        product.switch_to_product_tab()
        with allure.step("Select size"):
            product.select_size()
        with allure.step("Add to bag"):
            product.add_to_bag()

        with allure.step("Verify add to bag"):
            product.verify_add_to_bag()
        with allure.step("Open bag"):
            product.open_bag()
        with allure.step("Verify Item in bag"):
            product.verify_item_in_bag()
        with allure.step("Click place order"):
            product.click_place_order()

        logger.info("E2E completed")

    #POSITIVE TESTING
    def test_mens_tshirts_positive(self, driver):

        home = HomePage(driver)
        category = CategoryPage(driver)

        home.open_myntra()
        home.hover_genz()
        home.click_mens_tshirts()

        category.verify_page_loaded()
        category.verify_products_visible()

    # POSITIVE TESTING
    def test_mens_kurtas_positive(self, driver):

        home = HomePage(driver)
        category = CategoryPage(driver)

        home.open_myntra()
        home.hover_genz()
        home.click_mens_kurtas()

        category.verify_page_loaded()
        category.verify_products_visible()

    # POSITIVE TESTING
    def test_mens_shoes_positive(self, driver):

        home = HomePage(driver)
        category = CategoryPage(driver)

        home.open_myntra()
        home.hover_genz()
        home.click_mens_shoes()

        category.verify_page_loaded()
        category.verify_products_visible()

    # POSITIVE TESTING
    def test_skincare_positive(self, driver):

        home = HomePage(driver)
        category = CategoryPage(driver)

        home.open_myntra()
        home.hover_genz()
        home.click_skincare()

        category.verify_page_loaded()
        category.verify_products_visible()

    # NEGATIVE TESTING
    # NEGATIVE TESTING
    def test_jewellery_negative(self, driver):
        home = HomePage(driver)
        category = CategoryPage(driver)

        home.open_myntra()
        home.hover_genz()
        home.click_jewellery()

        category.verify_page_loaded()

        wrong_text = "Smartphones"

        actual = driver.title

        assert wrong_text not in actual
        logger.info("Smartphones not found on jewellery page ")
        print(
            f"Negative Test Passed: "
            f"'{wrong_text}' correctly not found on Jewellery page"
        )

    # NEGATIVE TESTING
    # NEGATIVE TESTING
    def test_heels_negative(self, driver):
        home = HomePage(driver)
        category = CategoryPage(driver)

        home.open_myntra()
        home.hover_genz()
        home.click_heels()

        category.verify_page_loaded()

        wrong_text = "Refrigerator"

        actual = driver.title

        assert wrong_text not in actual
        logger.info("Refrigerator not found on heels page ")
        print(
            f"Negative Test Passed: "
            f"'{wrong_text}' correctly not found on Heels page"
        )