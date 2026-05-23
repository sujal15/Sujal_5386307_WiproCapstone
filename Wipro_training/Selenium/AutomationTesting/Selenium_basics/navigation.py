import time
from cProfile import label
from re import search
from time import sleep

import locate
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Edge(service=Service('../Reasources/msedgedriver.exe'))

driver.get("https://www.wikipedia.com/")
time.sleep(3)

driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.back()
time.sleep(3)
driver.refresh()
time.sleep(3)

driver.quit()