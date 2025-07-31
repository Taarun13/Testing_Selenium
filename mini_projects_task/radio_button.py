from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://register.rediff.com/register/register.php")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@value='f']").click()
selected=driver.find_element(By.XPATH,"//input[@value='m']").is_selected()
print("Selected:",selected)
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='country']").click()
selected=driver.find_element(By.XPATH,"//input[@value='Cuba']").is_selected()
print("Selected:",selected)
time.sleep(5)
driver.quit()
