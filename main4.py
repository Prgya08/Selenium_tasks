import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

try:
    driver.get("https://www.amazon.in")
    time.sleep(2)

    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("laptops")
    search_box.send_keys(Keys.RETURN)

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span.a-size-medium"))
    )

    for _ in range(5):
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(2)

    product_elements = driver.find_elements(By.CSS_SELECTOR, "span.a-size-medium.a-color-base.a-text-normal")
    product_names = [el.text.strip() for el in product_elements if el.text.strip()]

    with open("amazon_products.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Product Name"])
        for name in product_names:
            writer.writerow([name])

    print(f"✅ {len(product_names)} product names saved to 'amazon_products.csv'")

finally:
    time.sleep(2)
    driver.quit()
