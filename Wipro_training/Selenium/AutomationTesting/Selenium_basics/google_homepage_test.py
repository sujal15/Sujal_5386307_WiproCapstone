# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# browser = input('What browser do you want to use?')
# match(browser.lower()):
#     case 'chrome':
#         driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#
#     case 'edge':
#         driver = webdriver.Edge(service=Service('../Reasources/msedgedriver.exe'))
#
#     case _:
#         print('Unknown browser - Not available \n Executing with default EDGE browser.')
#
# # driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
# driver.get('https://www.google.com')
# pagetitle = driver.title
# if pagetitle == 'Google':
#     print('Google Homepage loaded - Pass')
# else:
#     print('Google Homepage Not loaded - Fail')
#
# sleep(10)
#
# driver.quit()