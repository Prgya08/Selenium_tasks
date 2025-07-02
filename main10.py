import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://datatables.net/examples/server_side/simple.html")

wait = WebDriverWait(driver, 20)

# Wait for table to load
wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#example thead th")))

# Scroll the table into view (important!)
table_element = driver.find_element(By.ID, "example")
driver.execute_script("arguments[0].scrollIntoView();", table_element)
time.sleep(1)

# Create and write CSV
with open("ajax_table_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    
    # Write header
    headers = [th.text.strip() for th in driver.find_elements(By.CSS_SELECTOR, "#example thead th")]
    writer.writerow(headers)

    page = 1
    while True:
        print(f"📄 Scraping Page {page}...")

        # Wait for rows
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#example tbody tr")))

        rows = driver.find_elements(By.CSS_SELECTOR, "#example tbody tr")
        for row in rows:
            cols = [td.text.strip() for td in row.find_elements(By.TAG_NAME, "td")]
            if cols:
                writer.writerow(cols)

        # Scroll to pagination
        pagination = driver.find_element(By.ID, "example_paginate")
        driver.execute_script("arguments[0].scrollIntoView();", pagination)

        # Get next button and check if it's disabled
        try:
            next_btn = wait.until(EC.presence_of_element_located((By.ID, "example_next")))
            next_class = next_btn.get_attribute("class")
            if "disabled" in next_class:
                break  # No more pages
            next_btn.click()
            time.sleep(2)
            page += 1
        except Exception as e:
            print(f"❌ Error while trying to click next: {e}")
            break

driver.quit()
print("✅ Done. All rows saved in ajax_table_data.csv.")
