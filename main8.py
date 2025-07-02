from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def login_test(username,password):
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    time.sleep(1)

    message=driver.find_element(By.ID, "flash").text
    print(f"Login attempt with '{username}'/'{password}'")
    print("message", message.strip())
    
driver=webdriver.Chrome()
driver.maximize_window()

login_test("wronguser","wrongpassword")

login_test("tomsmith", "SuperSecretPassword!")

time.sleep(2)
driver.quit()
