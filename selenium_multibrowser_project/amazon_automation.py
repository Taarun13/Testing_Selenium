from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support.ui import Select

def run_amazon_flow():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.in")
    try:
        dropdown_element = driver.find_element(By.ID, "searchDropdownBox")
        dropdown = Select(dropdown_element)
        dropdown.select_by_visible_text("Video Games")
        search_box = driver.find_element(By.ID, "twotabsearchtextbox")
        time.sleep(2)
        search_box.send_keys("God of War")
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)
        driver.execute_script("window.scrollBy(0, 500);") 
        time.sleep(3)
        game = driver.find_element(By.XPATH, "//span[contains(text(), 'God of War Ragnorok')]")
        game.click()
        time.sleep(5)
        add_to_cart_button = driver.find_element(By.ID, "add-to-cart-button")
        add_to_cart_button.click()
        time.sleep(5)
        print("Amazon task running...")
        time.sleep(5)
    except Exception as e:
        print("Amazon Error:", e)
        driver.execute_script("alert('Amazon automation failed. Please check the error.');")
        time.sleep(5)
        driver.save_screenshot("amazon_error.png")
    finally:
        driver.quit()
