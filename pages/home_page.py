from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import allure
from utils.logger import logger
class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def open_myntra(self):

        self.driver.get("https://www.myntra.com")

        self.driver.maximize_window()

    def hover_genz(self):
        from selenium.webdriver.common.by import By
        from selenium.webdriver.common.action_chains import ActionChains
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        import time

        wait = WebDriverWait(self.driver, 30)

        # Wait for navbar
        wait.until(
            EC.presence_of_element_located(
                (By.TAG_NAME, "header")
            )
        )

        time.sleep(3)

        # REAL GENZ menu
        genz = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//a[@data-group='genz']"
                )
            )
        )

        # Scroll top
        self.driver.execute_script("window.scrollTo(0,0);")

        time.sleep(1)

        # Hover GENZ
        ActionChains(self.driver) \
            .move_to_element(genz) \
            .pause(3) \
            .perform()
        logger.info("Hovered on GENZ")
        print("Hovered on GENZ")
        allure.attach(
            "Hovered on GENZ successfully",
            name="Execution Log",
            attachment_type=allure.attachment_type.TEXT
        )
        time.sleep(5)

    def click_women_dresses(self):

        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        import time

        wait = WebDriverWait(self.driver, 30)

        time.sleep(3)

        # Find all visible submenu links
        links = self.driver.find_elements(By.TAG_NAME, "a")

        for link in links:

            text = link.text.strip()

            print("LINK FOUND:", text)

            if "Dresses" in text:
                self.driver.execute_script(
                    "arguments[0].click();",
                    link
                )
                logger.info("Clicked Women's Dresses")
                print("Clicked Dresses")
                allure.attach(
                    "Clicked Womens's Dresses category",
                    name="Dresses Navigation Log",
                    attachment_type=allure.attachment_type.TEXT
                )
                return

        raise Exception("Dresses link not found")

    def click_mens_tshirts(self):

        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        import time

        wait = WebDriverWait(self.driver, 30)

        time.sleep(3)

        # Locate MEN'S CASUAL WEAR section
        mens_section = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//li[contains(.,\"Men's Casual Wear\")]"
                )
            )
        )

        # Find all links inside that section
        links = mens_section.find_elements(By.TAG_NAME, "a")

        print("Links inside Men's Casual Wear:")

        for link in links:

            text = link.text.strip()

            print(text)

            if (
                    "T-Shirts" in text
                    or "Tshirts" in text
                    or "T-shirts" in text
            ):
                self.driver.execute_script(
                    "arguments[0].click();",
                    link
                )
                logger.info("Clicked Men's T-Shirts")
                print("Clicked Men's T-Shirts")
                allure.attach(
                    "Clicked Men's T-Shirts category",
                    name="Shirts Navigation Log",
                    attachment_type=allure.attachment_type.TEXT
                )
                return

        raise Exception("Men's T-Shirts link not found")

    def click_mens_kurtas(self):

        from selenium.webdriver.common.by import By
        import time

        time.sleep(5)

        links = self.driver.find_elements(By.TAG_NAME, "a")

        print("\nSearching Men's Kurtas...\n")

        inside_mens_section = False

        for link in links:

            try:

                text = link.text.strip()

                if text:
                    print("TEXT:", text)

                # Detect Men's Occassion Wear section
                if "Men'S Occassion Wear" in text:
                    inside_mens_section = True
                    print("\nFOUND MEN'S OCCASSION WEAR SECTION\n")
                    continue

                # Stop when next section starts
                if inside_mens_section and (
                        "Women'S Footwear" in text
                        or "Men'S Footwear" in text
                ):
                    inside_mens_section = False

                # Click only inside men's section
                if inside_mens_section:

                    if "Kurtas" in text:
                        print("\nFOUND MEN'S KURTAS LINK\n")

                        self.driver.execute_script(
                            "arguments[0].click();",
                            link
                        )
                        logger.info("Clicked Men's Kurtas")
                        print("Clicked Men's Kurtas")
                        allure.attach(
                            "Clicked Men's Kurtas category",
                            name="Kurta Navigation Log",
                            attachment_type=allure.attachment_type.TEXT
                        )
                        return

            except Exception as e:
                print("ERROR:", e)

        raise Exception("Men's Kurtas link not found")

    def click_mens_shoes(self):

        from selenium.webdriver.common.by import By
        import time

        time.sleep(5)

        links = self.driver.find_elements(By.TAG_NAME, "a")

        print("\nSearching Men's Casual Shoes...\n")

        inside_mens_footwear = False

        for link in links:

            try:

                text = link.text.strip()

                if text:
                    print("TEXT:", text)

                # Enter Men's Footwear section
                if "Men'S Footwear" in text:
                    inside_mens_footwear = True

                    print("\nFOUND MEN'S FOOTWEAR SECTION\n")

                    continue

                # Exit when next section starts
                if inside_mens_footwear and (
                        "Beauty & Grooming" in text
                        or "Accessories" in text
                ):
                    inside_mens_footwear = False

                # Click only inside Men's Footwear block
                if inside_mens_footwear:

                    if "Casual shoes" in text:
                        print("\nFOUND MEN'S CASUAL SHOES\n")

                        self.driver.execute_script(
                            "arguments[0].click();",
                            link
                        )
                        logger.info("Clicked Men's Shoes")
                        print("Clicked Men's Casual Shoes")
                        allure.attach(
                            "Clicked Men's Casual Shoes category",
                            name="Casual Shoes Navigation Log",
                            attachment_type=allure.attachment_type.TEXT
                        )
                        return

            except Exception as e:
                print("ERROR:", e)

        raise Exception("Men's Casual Shoes link not found")

    def click_skincare(self):

        from selenium.webdriver.common.by import By
        import time

        time.sleep(5)

        links = self.driver.find_elements(By.TAG_NAME, "a")

        print("\nSearching Skincare...\n")

        inside_beauty = False

        for link in links:

            try:

                text = link.text.strip()

                if text:
                    print("TEXT:", text)

                # Enter Beauty & Grooming section
                if "Beauty & Grooming" in text:
                    inside_beauty = True

                    print("\nFOUND BEAUTY & GROOMING SECTION\n")

                    continue

                # Exit when next section begins
                if inside_beauty and "Accessories" in text:
                    inside_beauty = False

                # Search only inside Beauty section
                if inside_beauty:

                    if "Skincare" in text:
                        print("\nFOUND SKINCARE LINK\n")

                        self.driver.execute_script(
                            "arguments[0].click();",
                            link
                        )
                        logger.info("Clicked Skincare")
                        print("Clicked Skincare")
                        allure.attach(
                            "Clicked Skincare category",
                            name="Skincare Log",
                            attachment_type=allure.attachment_type.TEXT
                        )
                        return

            except Exception as e:

                print("ERROR:", e)

        raise Exception("Skincare link not found")

    def click_jewellery(self):

        from selenium.webdriver.common.by import By
        import time

        time.sleep(5)

        links = self.driver.find_elements(By.TAG_NAME, "a")

        print("\nSearching Jewellery...\n")

        inside_accessories = False

        for link in links:

            try:

                text = link.text.strip()

                if text:
                    print("TEXT:", text)

                # Enter Accessories section
                if "Accessories" in text:
                    inside_accessories = True

                    print("\nFOUND ACCESSORIES SECTION\n")

                    continue

                # Exit when next section starts
                if inside_accessories and (
                        "STUDIO" in text
                        or "Wishlist" in text
                ):
                    inside_accessories = False

                # Search only inside Accessories section
                if inside_accessories:

                    if "Jewellery" in text:
                        print("\nFOUND JEWELLERY LINK\n")

                        self.driver.execute_script(
                            "arguments[0].click();",
                            link
                        )
                        logger.info("Clicked Jwellery")
                        print("Clicked Jewellery")
                        allure.attach(
                            "Clicked Jewellery category",
                            name="Jewellery Navigation Log",
                            attachment_type=allure.attachment_type.TEXT
                        )
                        return

            except Exception as e:

                print("ERROR:", e)

        raise Exception("Jewellery link not found")

    def click_heels(self):

        from selenium.webdriver.common.by import By
        import time

        time.sleep(5)

        links = self.driver.find_elements(By.TAG_NAME, "a")

        print("\nSearching Heels...\n")

        inside_women_footwear = False

        for link in links:

            try:

                text = link.text.strip()

                if text:
                    print("TEXT:", text)

                # Enter Women's Footwear section
                if "Women'S Footwear" in text:
                    inside_women_footwear = True

                    print("\nFOUND WOMEN'S FOOTWEAR SECTION\n")

                    continue

                # Exit when next section starts
                if inside_women_footwear and (
                        "Men'S Footwear" in text
                        or "Beauty & Grooming" in text
                ):
                    inside_women_footwear = False

                # Search only inside Women's Footwear
                if inside_women_footwear:

                    if "Heels" in text:
                        print("\nFOUND HEELS LINK\n")

                        self.driver.execute_script(
                            "arguments[0].click();",
                            link
                        )
                        logger.info("Clicked Heels")
                        print("Clicked Heels")
                        allure.attach(
                            "Clicked Women's Heels category",
                            name="Heels Navigation Log",
                            attachment_type=allure.attachment_type.TEXT
                        )
                        return

            except Exception as e:
                print("ERROR:", e)

        raise Exception("Heels link not found")