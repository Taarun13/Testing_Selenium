from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get('https://the-internet.herokuapp.com/checkboxes')
browser.maximize_window()
time.sleep(5)
checkboxes = browser.find_elements(By.XPATH, "//input[@type='checkbox']")
for checkbox in checkboxes:
    checkbox.send_keys(Keys.SPACE)
checked_count=0
for checkbox in checkboxes:
    if checkbox.is_selected():
        checked_count+=1
expected_checked_count=9
if checked_count == expected_checked_count:
    print('Checkbox count verified')
else:
    print('Checkbox count is mismatch')
time.sleep(5)
browser.close()
