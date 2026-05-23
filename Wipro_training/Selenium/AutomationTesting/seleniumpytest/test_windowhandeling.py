import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest_check as check

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/windows")
    yield driver
    driver.quit()

def test_multiple_window_handle(driver):
    wait = WebDriverWait(driver, 10)
    parent_window = driver.current_window_handle
    driver.find_element(By.LINK_TEXT, "Click Here").click()
    time.sleep(3)
    all_windows = driver.window_handles
    assert len(all_windows) == 2, "New Window did not open"

    for cwindow in all_windows:
        if cwindow != parent_window:
            driver.switch_to.window(cwindow)
            time.sleep(3)
            break

    time.sleep(3)
    header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h3"))).text
    assert header == "New Window", "New Window switch did not happen"

    time.sleep(3)
    driver.close()
    driver.switch_to.window(parent_window)
    time.sleep(3)
    assert driver.title == "The Internet", 'Parent Window switch did not happen'


def test_opem_multiple_tabs(driver):
    newwindowlink = driver.find_element(By.LINK_TEXT, "Click Here")

    