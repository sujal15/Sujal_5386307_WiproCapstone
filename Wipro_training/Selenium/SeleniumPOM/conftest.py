import time
import pytest
from selenium import webdriver


@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get('https://www.amazon.in')
    time.sleep(2)
    # driver.find_element(By.XPATH,"//button[text()='Continue shopping']").click()
    yield driver
    driver.quit()