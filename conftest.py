import pytest
import os
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

    # Take screenshot only if test failed
    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            folder = "screenshots"

            os.makedirs(folder, exist_ok=True)

            timestamp = datetime.now().strftime(
                "%Y%m%d_%H%M%S"
            )

            file_name = f"{item.name}_{timestamp}.png"

            path = os.path.join(
                folder,
                file_name
            )

            driver.save_screenshot(path)

            print(
                f"\nScreenshot saved: {path}"
            )


def pytest_sessionfinish(session, exitstatus):
    generate_reports()