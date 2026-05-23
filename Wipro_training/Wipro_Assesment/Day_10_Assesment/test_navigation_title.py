from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_nevigation_and_title(driver):
    driver.get("https://www.amazon.in")
    page_title = driver.title
    print("Page TItile:", page_title)
    print("Page Title:", page_title)
    assert "Amazon" in page_title
    mobiles = driver.find_elements(By.LINK_TEXT, "Mobiles")
    mobiles.click()
    driver.back()

