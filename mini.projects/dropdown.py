from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()  
driver.get("https://the-internet.herokuapp.com/dropdown")
driver.maximize_window()
time.sleep(2)
dropdown = driver.find_element(By.ID, "dropdown")
select = Select(dropdown)
select.select_by_visible_text("Option 2")  
time.sleep(2)
driver.quit()
