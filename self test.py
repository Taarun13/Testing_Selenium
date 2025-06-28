from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

service=Service(r"D:\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.chrome(service=service)
driver.get("https://www.google.com")
driver.maximize_window()
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("amazon")


