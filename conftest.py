import pytest
import os
import allure
from datetime import datetime
from utils.driver_setup import get_driver
from utils.report_generator import generate_reports

@pytest.fixture
def driver():

    driver = get_driver()

    yield driver

    driver.quit()


# Screenshot on test failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call":

        driver = item.funcargs.get("driver")

        if driver:

            os.makedirs("screenshots", exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            path = f"screenshots/{item.name}_{timestamp}.png"

            driver.save_screenshot(path)

            # Attach screenshot in Allure
            allure.attach.file(
                path,
                name="Test Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

            # Attach current page source
            allure.attach(
                driver.page_source,
                name="HTML Source",
                attachment_type=allure.attachment_type.HTML
            )


def pytest_sessionfinish(session, exitstatus):
    generate_reports()