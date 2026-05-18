"""
Behave environment.py
Manages WebDriver lifecycle, hooks, and screenshot-on-failure.
"""
import os
import logging
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from utils.config import Config
from utils.screenshot_utils import take_screenshot

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger("environment")


def before_all(context):
    context.config_data = Config()
    context.base_url = context.config_data.get("base_url", "https://www.myntra.com")
    logger.info(f"Test suite started — base URL: {context.base_url}")


def before_scenario(context, scenario):
    logger.info(f"▶ Scenario: {scenario.name}")
    browser = os.getenv("BROWSER", "chrome").lower()
    headless = os.getenv("HEADLESS", "false").lower() == "true"

    if browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        context.driver = webdriver.Firefox(options=options)
    else:
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        context.driver = webdriver.Chrome(options=options)

    context.driver.implicitly_wait(0)   # we use explicit waits only
    context.driver.maximize_window()
    context.initial_bag_count = 0
    logger.info(f"Browser launched: {browser}")


def after_scenario(context, scenario):
    if scenario.status == "failed":
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_name = scenario.name.replace(" ", "_").replace("/", "-")[:60]
        path = take_screenshot(context.driver, f"FAIL_{safe_name}_{ts}")
        logger.error(f"❌ Scenario FAILED — screenshot: {path}")
    else:
        logger.info(f"✅ Scenario PASSED: {scenario.name}")

    if hasattr(context, "driver") and context.driver:
        context.driver.quit()
        logger.info("Browser closed")


def after_all(context):
    logger.info("Test suite finished")
