import pytest
from pages.loginpage import LoginPage
from utils.csv_reader import CSVReader
from utils.logger import LogGen

from utils.excel_reader import ExcelReader
logger = LogGen.loggen()

@pytest.mark.order(1)
@pytest.mark.parametrize(
    "data",
    CSVReader.read_csv("login_data.csv")
    # ExcelReader.read_excel("test_data.odx", "login_data")
)
def test_login(driver, data):
    login_page = LoginPage(driver)
    logger.info(f'Login Page opened')
    logger.info(f'Trying to ogin with data - {data{"username"}}, {data{"password"}}')
    login_page.login(data["username"], data["password"])

    logger.info(f'Checking logged status')
    if data["expected_result"] == "success":
        assert "inventory" in driver.current_url
        screenshot_path = screenshotUtil.capture_screenshot(driver, screenshot_name='login_test')
    else:
        assert "inventory" not in driver.current_url
        assert login_page.read_error_message()._contains_("do not match")
        logger.setLevel(f'Screenshot ')
        screenshot_path = screenshotUtil.capture_screenshot(driver, screenshot_name='login_test')
