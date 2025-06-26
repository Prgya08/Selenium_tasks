from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Set Chrome options
options = Options()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--disable-web-security")
options.add_argument("--disable-popup-blocking")

# Create driver with options
driver = webdriver.Chrome(options=options)

try:
    driver.get("https://prgya08.github.io/form/form.html")
    time.sleep(4)

    driver.execute_script("window.scrollBy(0, 500);")

    first_name = driver.find_element(By.NAME, "firstname")
    last_name = driver.find_element(By.NAME, "lastname")

    first_name.clear()
    first_name.send_keys("Pragya")

    last_name.clear()
    last_name.send_keys("Sharma")

    submit = driver.find_element(By.XPATH, "//form[@action='/action_page.php']//input[@type='submit']")
    submit.click()

    print("✅ Form submitted successfully!")
    time.sleep(4)

    driver.execute_script("alert('Form submitted successfully!')")
    time.sleep(3)


finally:
    driver.quit()
