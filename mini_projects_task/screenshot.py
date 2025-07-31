from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("https://www.google.com")
#script_executor
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

driver.save_screenshot("google_home.png")
print("Screenshot taken!")
