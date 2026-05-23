import time
from cProfile import label
from re import search
from time import sleep
import pytest
import locate
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://www.amazon.in")
    yield driver
    driver.quit()


def test_open_amazon(driver):
    assert 'amazon' in driver.current_url.lower(), f"Unexpected URL: {driver.current_url}"
    assert 'amazon' in driver.title.lower(), f"Unexpected Title: {driver.title}"
    print("\nOpened Amazon Homepage. Title verified")


def test_search_product(driver):
    wait = WebDriverWait(driver, 5)

    search_box = wait.until(
        EC.presence_of_element_located((By.ID, 'twotabsearchtextbox'))
    )

    search_box.clear()
    search_box.send_keys("wirelesss mouse")

    search_button = driver.find_element(By.ID, "nav-search-submit-button")
    search_button.click()

    assert 'wireless' in driver.current_url.lower(), 'Search result page did not load'

    print("\nSearch result page loaded successfully")


def test_find_element_amazon(driver):
    wait = WebDriverWait(driver, 15)

    # First product element
    first_product = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "a h2 span"))
    )
    print("\nFirst Product:", first_product.text)

    # All product titles
    product_titles = driver.find_elements(By.CSS_SELECTOR, "a h2 span")  # corrected: find_elements returns a list
    print(f"\nFound {len(product_titles)} product titles on page one.\n")

    # Enumerate first 5 products
    for i, title in enumerate(product_titles[:5], start=1):  # corrected 'strt' to 'start'
        print(f"{i}. {title.text}")

    assert len(product_titles) > 0, "No product found on Amazon search result"