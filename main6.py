from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up WebDriver (make sure chromedriver is installed and in PATH)
driver = webdriver.Chrome()

try:
    # 1. Open the page
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

    # 2. Wait for the "Start" button to become clickable
    start_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button"))
    )

    # 3. Click the "Start" button
    start_button.click()

    # 4. Wait for the result text to appear (element is visible)
    result_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "finish"))
    )

    # 5. Print the result text
    print("Result:", result_text.text)

finally:
    driver.quit()
