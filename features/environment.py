from utils.driver_setup import get_driver
import allure
import os
from datetime import datetime
from utils.logger import logger

def before_scenario(context, scenario):
    logger.info(f"Starting scenario: {scenario.name}")

    context.driver = get_driver()


def after_step(context, step):

    # Capture screenshot only if step fails
    if step.status == "failed":

        os.makedirs(
            "screenshots",
            exist_ok=True
        )

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        path = (
            f"screenshots/"
            f"{step.name}_{timestamp}.png"
        )

        context.driver.save_screenshot(
            path
        )

        print(
            f"Screenshot saved: {path}"
        )

        # Attach screenshot into Allure
        with open(path, "rb") as file:

            allure.attach(
                file.read(),
                name="Failure Screenshot",
                attachment_type=
                allure.attachment_type.PNG
            )


def after_scenario(context, scenario):
    logger.info(f"Completed scenario: {scenario.name}")
    os.makedirs(
        "screenshots",
        exist_ok=True
    )

    path = f"screenshots/{scenario.name}.png"

    context.driver.save_screenshot(path)

    with open(path,"rb") as file:

        allure.attach(
            file.read(),
            name=scenario.name,
            attachment_type=
            allure.attachment_type.PNG
        )

    context.driver.quit()