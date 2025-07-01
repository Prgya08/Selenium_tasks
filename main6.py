from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

    start_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button"))
    )

    start_button.click()

    result_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "finish"))
    )

    print("Result:", result_text.text)

finally:
    driver.quit()
