import logging
import os
import sys
import argparse
from os.path import join

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.auto.pages.review_page import ReviewPage
from src.tools import logger_util

logger = logger_util.initialize_logger("review_app.txt", __name__, logging.DEBUG)
SCREENSHOT_NAME = join(os.getcwd(), "reviews-failed.png")
LOG_FILE_PATH = join(os.getcwd(), "review_app.txt")


class SmokeShopReviewScraper:
    def __init__(self):
        self.options = Options()
        self.options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=Service(), options=self.options)
        self.wait = WebDriverWait(self.driver, 10)
        logger.info("Initialized ChromeDriver and WebDriverWait")

    def run(self):
        try:
            stores = self.get_store_names()
            logger.info(f"Found {len(stores)} stores.")

            for store in stores:
                logger.info(f"Searching reviews for: {store}")
                self.scrape_reviews_for_store(store)

            logger.info("✅ All reviews scraped successfully.")
        except Exception as e:
            self._take_screenshot(SCREENSHOT_NAME)
            logger.exception(f"❌ Error during execution: {e}", exc_info=True)
            raise
        finally:
            self.driver.quit()

    def get_store_names(self):
        self.driver.get("https://www.elpasosmokeshops.com/locations/")
        self.driver.implicitly_wait(5)

        for _ in range(6):
            self.driver.execute_script("window.scrollBy(0, 500);")

        headings = self.driver.find_elements(By.TAG_NAME, "h2")
        store_names = [h.text.strip() for h in headings if h.text.strip().endswith("Smoke Shop")]
        return store_names

    def scrape_reviews_for_store(self, store_name):
        self.driver.get("https://www.google.com/maps")
        try:
            self.wait.until(EC.presence_of_element_located((By.ID, "searchboxinput"))).send_keys(
                store_name + " El Paso TX", Keys.RETURN
            )
            logger.info(f"🔍 Searched for {store_name} on Google Maps")

            self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@aria-label, " reviews")]'))).click()
            logger.info("📃 Clicked on View All Reviews")

            for _ in range(5):
                self.driver.execute_script(r"document.querySelector('div[role=\"main\"]').scrollBy(0, 300);")

            page = ReviewPage(self.driver)
            reviews = page.get_reviews_data()
            logger.info(f"✅ Found {len(reviews)} reviews for {store_name}")

            for review in reviews:
                logger.debug(f"{review['username']} | {review['date']} | {review['rating']} | {review['text']}")

        except Exception as e:
            logger.warning(f"⚠️ Could not fetch reviews for {store_name}: {e}")

    def _take_screenshot(self, screenshot_path: str):
        try:
            self.driver.save_screenshot(screenshot_path)
        except Exception as e:
            logger.error(f"Error taking screenshot: {e}")


def main():
    parser = argparse.ArgumentParser(description="Run Smoke Shop Review Scraper")
    parser.add_argument("--force", action="store_true", help="Force run the review scraper")
    args = parser.parse_args()

    logger.info("🚀 Starting Smoke Shop Review Scraper")
    SmokeShopReviewScraper().run()
    return 0


if __name__ == "__main__":
    sys.exit(main())
