from selenium import webdriver
from selenium.webdriver.chrome.options import ChromiumOptions

options = ChromiumOptions()
driver = webdriver.Chrome(options=options)
try:
    driver.get("https://google.com")
    page_title= driver.title
    assert page_title== "Google", (f"Expected title 'Google' but got {page_title}")

    print("title verification")

except:
    print(f"not found {page_title}")

finally:
    driver.quit()


