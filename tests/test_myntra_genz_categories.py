import pytest
import logging
from pages.home_page import HomePage
from pages.product_page import ProductPage

@pytest.mark.usefixtures("setup")
class TestMyntraGenZCategories:

    @pytest.fixture(autouse=True)
    def reset_browser_state(self):
        yield
        base = BasePage(self.driver)
        base.close_tabs_except_root()

    def test_01_e2e_womens_western_dresses(self):
        logging.info("Executing: TC_01_E2E_Women_Western_Dresses")
        home = HomePage(self.driver)
        home.search_genz_category("Women Dresses")
        product = ProductPage(self.driver)
        assert product.is_element_present(ProductPage.FIRST_PRODUCT_CARD)
        product.select_first_product()
        product.choose_available_size()
        product.click_add_to_bag()
        product.go_to_checkout_bag()
        assert "checkout/cart" in self.driver.current_url

    def test_02_pos_mens_casual_tshirts(self):
        logging.info("Executing: TC_02_Pos_Mens_Casual_Tshirts")
        home = HomePage(self.driver)
        home.search_genz_category("Men T-shirts")
        product = ProductPage(self.driver)
        assert product.is_element_present(ProductPage.FIRST_PRODUCT_CARD)

    def test_03_pos_mens_occasion_kurtas(self):
        logging.info("Executing: TC_03_Pos_Mens_Occasion_Kurtas")
        home = HomePage(self.driver)
        home.search_genz_category("Men Kurtas")
        product = ProductPage(self.driver)
        product.select_first_product()
        assert product.is_element_present(ProductPage.PRODUCT_NAME_HEADER)

    def test_04_pos_mens_footwear_shoes(self):
        logging.info("Executing: TC_04_Pos_Mens_Footwear_Shoes")
        home = HomePage(self.driver)
        home.search_genz_category("Men Casual Shoes")
        product = ProductPage(self.driver)
        assert product.is_element_present(ProductPage.FIRST_PRODUCT_CARD)

    def test_05_pos_beauty_skincare(self):
        logging.info("Executing: TC_05_Pos_Beauty_Skincare")
        home = HomePage(self.driver)
        home.search_genz_category("Skincare Beauty")
        product = ProductPage(self.driver)
        assert product.is_element_present(ProductPage.FIRST_PRODUCT_CARD)

    def test_06_neg_accessories_jewellery_no_size(self):
        logging.info("Executing: TC_06_Neg_Accessories_Jewellery_No_Size")
        home = HomePage(self.driver)
        home.search_genz_category("Jewellery Rings")
        product = ProductPage(self.driver)
        product.select_first_product()
        product.click_add_to_bag()
        assert product.is_element_present(ProductPage.SIZE_ERROR_BUBBLE)

    def test_07_neg_womens_footwear_heels(self):
        logging.info("Executing: TC_07_Neg_Womens_Footwear_Heels_Gibberish")
        home = HomePage(self.driver)
        home.search_genz_category("Heels INVALID_GIBBERISH_QUERY_INJECTION")
        product = ProductPage(self.driver)
        assert product.is_element_present(ProductPage.NO_PRODUCTS_ERROR)