from selenium.webdriver.common.by import By
from src.auto.pages.base_element import BaseElement


class ReviewPage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def usernames(self):
        return BaseElement(self.driver, (By.CLASS_NAME, 'd4r55'))

    @property
    def review_dates(self):
        return BaseElement(self.driver, (By.CLASS_NAME, 'rsqaWe'))

    @property
    def review_ratings(self):
        return BaseElement(self.driver, (By.CSS_SELECTOR, 'span[role="img"]'))

    @property
    def review_texts(self):
        return BaseElement(self.driver, (By.CLASS_NAME, 'wiI7pd'))

    def get_reviews_data(self):
        usernames = self.usernames._find_elements()
        dates = self.review_dates._find_elements()
        ratings = self.review_ratings._find_elements()
        texts = self.review_texts._find_elements()

        reviews = []
        for i in range(min(len(usernames), len(dates), len(ratings), len(texts))):
            user = usernames[i].text.strip()
            date = dates[i].text.strip()
            rating = ratings[i].get_attribute("aria-label").strip()
            text = texts[i].text.strip()
            reviews.append({
                "username": user,
                "date": date,
                "rating": rating,
                "text": text
            })
        return reviews
