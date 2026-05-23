import time
from time import sleep
import locate
from requests import options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Edge()
driver.maximize_window()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")
time.sleep(1)


# text_input--
text_input = driver.find_element(By.ID, "my-text-id")
text_input.clear()
text_input.send_keys("Selenium WebDriver Demo")

# text_password--
password_input = driver.find_element(By.NAME, "my-password")
password_input.clear()
password_input.send_keys("secret123")

# text_area--
text_area = driver.find_element(By.NAME, "my-textarea")
text_area.clear()
text_area.send_keys("This is a simple message ")

# checkbox--
checkbox = driver.find_element(By.ID, "my-check-2")
checkbox.click()

# radio--
radio = driver.find_element(By.ID, "my-radio-2")
radio.click()

#dropdown
dropdown = driver.find_element(By.NAME, "my-select")
dropdown.click()
option = driver.find_element(By.CSS_SELECTOR, "select[name = 'my-select'] option[value='2']")
option.click()

# datalist--
multi_select = driver.find_element(By.NAME, "my-datalist")
multi_select.send_keys('New York')

# filr_upload--
file_upload = driver.find_element(By.NAME, "my-file")
file_upload.send_keys("C:\\Wipro Training\\AutomationTesting\\Selenium_basics\\wait.py")

# range--
range_slider = driver.find_element(By.NAME , "my-range")
driver.execute_script("arguments[0].value = 10;", range_slider)

# color_picker--
color_picker = driver.find_element(By.NAME, "my-colors")
color_picker.send_keys("#00ff00")

# date picker--
date_input = driver.find_element(By.NAME, "my-date")
date_input.send_keys("2025-12-25")

# submit option --
submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
time.sleep(20)
submit_btn.click()

time.sleep(10)
driver.quit()