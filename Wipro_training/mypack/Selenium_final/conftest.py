import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager

from utils.config_reader import ConfigReader
from utils.logger import LogGen

logger = LogGen.loggen()

@pytest.fixture(scope="function")
def driver():
    browser = ConfigReader.get("browser").strip() .lower()
    logger.info(f'==========================')
    logger.info('Starting test')
    logger.info'Reading Configiration'
    print(f"Browser from config: '{browser}'")
    logger.info

    base_url = ConfigReader.get("base_url").strip() .lower()

    headless = ConfigReader.get("headless").strip()

    if browser == "edge":
            edge_options = EdgeOptions()
            edge_options.add_argument("--start-maximized")
            edge_options.add_argument("--disable-notifications")
            edge_options.add_argument("--disable-infobars")
            edge_options.add_argument("--disable-extensions")
            if headless:
                edge_options.add_argument("--headless")
            driver = webdriver.Edge(
                service=EdgeService("resources/msedgedriver.exe"),
                options=edge_options
            )
    elif browser == "chrome":
            chrome_options = ChromeOptions()
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--disable-notifications")
            chrome_options.add_argument("--disable-infobars")
            chrome_options.add_argument("--disable-extensions")
            if headless:
                chrome_options.add_argument("--headless")
            driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=chrome_options
            )
    else:
        driver = webdriver.Edge(
            service=EdgeService("resources/msedgedriver.exe")
        )
    logger.info(f'Opened the browser: {browser}')
    driver.get(base_url)
    logger.info(f'URL Loaded: {base_url}')
    yield driver
    driver.quit()
    logger.info(f'Closing Browser: {browser}')
    logger.info(f"Ending test")
    logger.info(f'==========================================')