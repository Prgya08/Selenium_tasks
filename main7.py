from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome() 
driver.maximize_window()

# Step 2: Open the website
driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.LINK_TEXT, "Click Here").click()

main_window = driver.current_window_handle
all_windows = driver.window_handles

for handle in all_windows:
    if handle != main_window:
        driver.switch_to.window(handle)
        break

heading = driver.find_element(By.TAG_NAME, "h3").text
print("Heading in new tab:", heading)

driver.close()
driver.switch_to.window(main_window)

print("Back to original window:", driver.title)

time.sleep(2)
driver.quit()
