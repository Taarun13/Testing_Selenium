from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.google.com")
wait = WebDriverWait(driver, 5)
logo = wait.until(EC.presence_of_element_located((By.XPATH, "//img[@alt='Google']")))
src = logo.get_attribute("src")
print("Logo source attribute:", src)
driver.quit()
