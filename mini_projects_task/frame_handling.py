from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_iframe")
driver.maximize_window()
driver.switch_to.frame("iframeResult")
driver.switch_to.frame(0)
print("Inner frame title:", driver.title)
driver.switch_to.default_content()
time.sleep(3)
driver.quit()
