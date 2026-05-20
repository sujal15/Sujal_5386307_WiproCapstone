from pages.home_page import HomePage
from pages.category_page import CategoryPage
from pages.product_page import ProductPage
import time


class TestGENZCategories:

    #E2E TESTING
    def test_womens_dresses_e2e(self, driver):

        home = HomePage(driver)
        category = CategoryPage(driver)
        product = ProductPage(driver)

        home.open_myntra()
        home.hover_genz()
        home.click_women_dresses()

        category.verify_page_loaded()
        category.verify_products_visible()
        category.open_first_product()

        product.switch_to_product_tab()
        product.select_size()
        product.add_to_bag()
        product.verify_add_to_bag()

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
    def test_jewellery_negative(self, driver):
        home = HomePage(driver)
        category = CategoryPage(driver)

        home.open_myntra()

        home.hover_genz()

        home.click_jewellery()

        category.verify_page_loaded()

        # Intentionally wrong expectation
        expected_title = "Mobiles"

        actual_title = driver.title

        assert expected_title in actual_title, \
            f"Negative test passed: '{expected_title}' not found"

    # NEGATIVE TESTING
    def test_heels_negative(self, driver):
        home = HomePage(driver)
        category = CategoryPage(driver)

        home.open_myntra()

        home.hover_genz()

        home.click_heels()

        category.verify_page_loaded()

        # Intentionally wrong expectation
        expected = "Laptop"

        actual = driver.title

        assert expected in actual, \
            f"Negative test passed: '{expected}' not found"