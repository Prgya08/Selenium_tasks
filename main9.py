import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

upload_file = os.path.abspath("test_upload.txt")  
download_dir = os.path.abspath("downloads")
os.makedirs(download_dir, exist_ok=True)

options = Options()
prefs = {"download.default_directory": download_dir}
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/upload")

upload_input = driver.find_element(By.ID, "file-upload")
upload_input.send_keys(upload_file)
driver.find_element(By.ID, "file-submit").click()
time.sleep(2)

upload_name = driver.find_element(By.ID, "uploaded-files").text
print(f"Uploaded file: {upload_name}")
assert upload_name == os.path.basename(upload_file), "Uploaded filename mismatch"

driver.get("https://the-internet.herokuapp.com/download")
driver.find_element(By.LINK_TEXT, "some-file.txt").click()
time.sleep(2)

download_file = os.path.join(download_dir, "some-file.txt")
if os.path.exists(download_file):
    print(f"File downloaded successfully: {download_file}")
else:
    print(" Download failed!")

time.sleep(2)
driver.quit()
