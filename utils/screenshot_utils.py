"""utils/screenshot_utils.py — saves screenshots to reports/screenshots/"""
import os
from datetime import datetime

SCREENSHOT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "reports", "screenshots")


def take_screenshot(driver, name="screenshot"):
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)
    filename = f"{name}.png"
    filepath = os.path.join(SCREENSHOT_DIR, filename)
    driver.save_screenshot(filepath)
    return filepath
