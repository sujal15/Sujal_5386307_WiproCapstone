from selenium import webdriver
from selenium.webdriver.ie.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

driver = webdriver.Edge(service=Service('../Reasources/msedgedriver.exe'))
driver.get('https://www.google.com')
pagetitle = driver.title
if pagetitle == 'Google':
    print()
else:
    print()
time.sleep(20)
driver.quit()


