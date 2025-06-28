from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

service = Service(r"D:\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")
time.sleep(3)
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("amazon")
search_box.send_keys(Keys.RETURN)
time.sleep(100)

