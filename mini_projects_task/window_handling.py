from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_win_open")
driver.maximize_window()
driver.switch_to.frame("iframeResult")
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(2)
windows = driver.window_handles
driver.switch_to.window(windows[1])
print("New window/tab title:", driver.title)
driver.close()
driver.switch_to.window(windows[0]) 
driver.quit()
