from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://google.com")
assert "Google" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("Selenium Python")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

results = driver.find_elements(By.CSS_SELECTOR, "div.g")
if results:
    print(f"✅ Search results found: {len(results)} results displayed.")
else:
    print("❌ No results found.")
time.sleep(20)
driver.close()