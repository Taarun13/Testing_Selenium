from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
rows = driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr")
for row in rows:
    columns = row.find_elements(By.TAG_NAME, "td")
    row_data = [col.text for col in columns]
    if row_data: 
        print("Row:", row_data)
driver.quit()
