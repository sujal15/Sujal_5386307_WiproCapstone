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



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver = webdriver.Edge(service=Service('../Reasources/msedgedriver.exe'))

driver.get('https://www.google.com')


# id---
# search_input = driver.find_element(By.ID , 'APjFqb' )
# search_input.send_keys('selenium')
# time.sleep(3)
# search_input.clear()
# time.sleep(3)


# name--
# search_input = driver.find_element(By.NAME , 'q' )
# search_input.send_keys('locators')
# time.sleep(30)


# class--
# googlesearch_button = driver.find_element(By.CLASS_NAME,'RNmpXc')
# googlesearch_button.click()
# time.sleep(30)


# tag name--
# href_elements = driver.find_elements(By.TAG_NAME,'a')
# for elmt in href_elements:
#     print(f'{elmt.text} - {elmt.get_attribute('href')}')


# linktext--
# image_link = driver.find_elements(By.LINK_TEXT, 'Images')
# image_link.click()
# time.sleep(30)


# partiallink text--
# image_link = driver.find_elements(By.PARTIAL_LINK_TEXT, 'ma')
# image_link.click()
# time.sleep(30)


# css selector--
# search_input = driver.find_element(By.CSS_SELECTOR, 'div > textarea')
# search_input.send_keys('selenium')
# time.sleep(30)


# driver.get("https://the-internet.herokuapp.com/tables")
# time.sleep(3)

# and operator --
# setting_test = driver.find_elements(By.XPATH, '/html/body/div[2]/div[4]/form/div[1]/div/div[1]/div[1]/div[3]/textarea')
# print(setting_test.text)
# time.sleep(5)


# and or operator --
# and_example = driver.find_elements(By.XPATH, "//td[text()='Tim' and text()='first-name]")
# print(f"AND Example found with both the conditions: {and_example.text} ")
# or_example = driver.find_elements(By.XPATH, "//td[test()='Tim' or text()='Frank']")
# print(f"OR Example found with both the conditions: {or_example.text} ")



# rows = driver.find_elements(By.XPATH, "//table[@id='table']/tbody/tr/td]")
# print(f"Child Example found:{len(rows)} column in the first table")
# email_cell = driver.find_elements(By.XPATH, "//table[@id='table1]//td[text()'jdoe@hotmail.com']")
# parent_row = driver.find_elements(By.XPATH, "//table[@id='table1']//td[text()='jdoe@hotmail.com']/parent::tr")
# print(f"Parent Example Email '{email_cell.text}' belongs to row with first name: "
#       f"{parent_row.find_element(By.XPATH, './td[2]').text}")



# Find all rows in the first table
# rows = driver.find_elements(By.XPATH, "//table[@id='table1']/tbody/tr/td")
# print(f"Child Example found: {len(rows)} columns in the first table")



# # Find the cell containing the specific email
# email_cell = driver.find_elements(By.XPATH, "//table[@id='table1']//td[text()='jdoe@hotmail.com']")
#
# # Get the parent row of that email cell
# parent_row = driver.find_elements(By.XPATH, "//table[@id='table1']//td[text()='jdoe@hotmail.com']/parent::tr")
# print(f"Parent Example Email '{email_cell.text}' belongs to row with first name: "f"{parent_row.find_element(By.XPATH, './td[2]').text}")
# ancestor_table = driver.find_element(By.XPATH, "//td[text()='jdoe@hotmail.com']/ancestor::table")
# print(f"Ancestor Example table ID: {ancestor_table.get_attribute('id')}")

# Reelative locator
# driver.get("https://www.saucedemo.com/")
# time.sleep(5)
# username_field = driver.find_element(By.ID, "user-name")
# password_field = driver.find_element(By.ID, "password")
# login_button = driver.find_element(By.ID, "login-button")
# elmt_above_password = driver.find_element(locate_with(By.TAG_NAME, "input").above(password_field))
# print(f"Above Example Text above password: {elmt_above_password.get_attribute('placeholder')}")
# elmt_above_password.send_keys('standard_user')
# time.sleep(5)
# field_below_username = driver.find_element(locate_with(By.TAG_NAME, "input").below(username_field))
# print(f"Below Example Placeholder below username: {field_below_username.get_attribute('placeholder')}")
# field_below_username.send_keys('secret_sauce')
# time.sleep(2)
# login_button.click()
# time.sleep(2)
# twitter_icon = driver.find_element(By.LINK_TEXT, "Twitter")
# facbook_icon = driver.find_element(locate_with(By.TAG_NAME, "a").to_right_of(twitter_icon))
# print(f"toleftOf Example Elemnet to the left of Twitter icon has href: {facbook_icon.get_attribute("href")}")
# left_icon = driver.find_element(locate_with(By.TAG_NAME, "a").to_left_of(facbook_icon))
# print(f"toRightOf Example Element to the right of Twitter icon has href: {left_icon.get_attribute("href")}")
# near_twitter = driver.find_element(locate_with(By.TAG_NAME, "a").near(twitter_icon))
# print(f"Near Example Element near Twitter icon has href: {near_twitter.get_attribute("href")}")
# time.sleep(3)
# driver.quit()