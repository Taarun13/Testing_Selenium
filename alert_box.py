from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
import time

service = Service(r"D:\chromedriver-win64\chromedriver-win64\chromedriver.exe")  
driver = webdriver.Chrome(service=service)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
alert = Alert(driver)
print("Alert says:", alert.text)
alert.accept()
time.sleep(3)
driver.quit()
