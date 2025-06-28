from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
driver.quit()