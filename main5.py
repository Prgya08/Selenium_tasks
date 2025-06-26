import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

# Set up driver
driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
driver.maximize_window()
time.sleep(2)

# Locate the dropdown (select element)
dropdown = Select(driver.find_element(By.NAME, "my-select"))

# Select an option by visible text
dropdown.select_by_visible_text("Two")
time.sleep(2)

# Take screenshot
driver.save_screenshot("dropdown_selected.png")
print("✅ Screenshot taken after selecting dropdown option.")

driver.quit()
