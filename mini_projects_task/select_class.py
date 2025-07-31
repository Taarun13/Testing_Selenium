from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://www.ebay.com")
driver.maximize_window()

dropdown = Select(driver.find_element(By.ID, "gh-cat"))
for option in dropdown.options:
    print(option.text)
    dropdown.select_by_visible_text("Music")  
time.sleep(2)
driver.find_element(By.ID, "gh-btn").click()
driver.quit()
