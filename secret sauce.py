from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(r"D:\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

username = driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")  
password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce") 

login_button = driver.find_element(By.ID, "login-button")
login_button.click()

time.sleep(5)