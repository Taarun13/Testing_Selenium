from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

service = Service(r"D:\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.youtube.com/")
time.sleep(5)
search_box = driver.find_element(By.NAME, "search_query")
search_box.send_keys("selenium freecodecamp")
search_box.send_keys(Keys.RETURN)
time.sleep(3)
video = driver.find_element(By.XPATH, "//a[contains(@title, 'Selenium') and contains(@href, 'watch')]")
video.click()
time.sleep(10)
next_video_button = driver.find_element(By.XPATH, "//a[@class='ytp-next-button ytp-button']")
next_video_button.click()
time.sleep(10)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.refresh()
time.sleep(5)
driver.quit()