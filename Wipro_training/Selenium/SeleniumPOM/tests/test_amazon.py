import pytest

from pages.homepage import HomePage
from pages.product_listing_page import ProductListingPage


def test_open_amazon(driver):
    assert "amazon" in driver.current_url, 'URL for amazon is not correct'
    print("\nOpened Amazon Homepage. Title & URL verified!")


@pytest.mark.parametrize("search_product", [
    ("wireless mouse"),
    ("shoes")
])
def test_search_product(driver, search_product):
    homepage = HomePage(driver)

    homepage.type_search_input(search_product)
    print(f"Searching product - {search_product}")
    homepage.click_search_button()

    assert homepage.is_amazon_page_loaded() == True, 'Search results page did not load.'
    print("\nSearch results page loaded successfully")


@pytest.mark.parametrize("search_product", [
    ("wireless mouse"), ("shoes")
])
def test_find_elements_amazon(driver, search_product):
    homepage = HomePage(driver)

    homepage.type_search_input(search_product)
    homepage.click_search_button()

    assert homepage.is_amazon_page_loaded(), 'Search results page did not load.'
    print("\nSearch results page loaded successfully")

    productlistingpage = ProductListingPage(driver)

    productlistingpage.find_product_title()
    val = productlistingpage.all_products()

    assert val, "No products found on Amazon search results!"


@pytest.mark.parametrize(("search_product", "brandname"), [
    ("wireless mouse", "Logitech"),
    ("shoes", "Nike")
])
def test_brand_filter(driver, search_product, brandname):
    homepage = HomePage(driver)

    homepage.type_search_input(search_product)
    print(f"\nSearching product - {search_product}")
    homepage.click_search_button()

    assert homepage.is_amazon_page_loaded(), 'Search results page did not load.'
    print(f"\nSearch results page loaded successfully - {search_product}")

    productlistingpage = ProductListingPage(driver)

    productlistingpage.select_brand_filter(brandname)

    assert productlistingpage.check_product_titles_for_brand_filter(brandname), 'Brand filter did not apply'