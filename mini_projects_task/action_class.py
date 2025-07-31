from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://www.amazon.in")
driver.maximize_window()

menu = driver.find_element(By.ID, "nav-link-accountList")
ActionChains(driver).move_to_element(menu).perform()
print("Hovered over Account & Lists")

time.sleep(5) 
driver.quit()
