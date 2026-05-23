import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    yield driver
    driver.quit()

def test_simple_js_alert(driver):
    driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
    alert = driver.switch_to.alert
    assert alert.text == "I am a JS Alert", 'Alert was wrong'
    time.sleep(3)
    alert.accept()
    time.sleep(3)
    result = driver.find_element(By.ID, "result").text
    assert "You successfully clicked an alert" in result, "Result text was wrong"

def test_js_confirmdismiss(driver):
    driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
    alert = driver.switch_to.alert
    time.sleep(3)
    assert alert.text == "I am a JS Confirm"
    alert.dismiss()
    time.sleep(3)
    result = driver.find_element(By.ID, "result").text
    assert "You clicked: Cancel" in result, "Result text was wrong"


def test_js_confirmok(driver):
    driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
    alert = driver.switch_to.alert
    time.sleep(3)
    assert alert.text == "I am a JS Confirm"
    alert.accept()
    time.sleep(3)
    result = driver.find_element(By.ID, "result").text
    assert "You clicked: Ok" in result, "Result text was wrong"


def test_js_prompt(driver):
    driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
    alert = driver.switch_to.alert
    time.sleep(3)
    assert alert.text.lower() == "i am a js prompt", 'Alert text was wrng'
    time.sleep(3)
    alert.accept()
    time.sleep(3)
    result = driver.find_element(By.ID, "result").text
    assert "You entered:" in result, "Result text was wrong"