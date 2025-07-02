from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from logger import log_step

def run_amazon_flow():
    module = "Amazon"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.in")
    try:
        log_step(module, "Opened Amazon homepage", "Pass")
        dropdown_element = driver.find_element(By.ID, "searchDropdownBox")
        dropdown = Select(dropdown_element)
        dropdown.select_by_visible_text("Video Games")
        log_step(module, "Selected 'Video Games' from dropdown", "Pass")
        search_box = driver.find_element(By.ID, "twotabsearchtextbox")
        time.sleep(2)
        search_box.send_keys("God of War")
        log_step(module, "Entered search term 'God of War'", "Pass")
        search_box.send_keys(Keys.RETURN)
        log_step(module, "Submitted search", "Pass")
        time.sleep(3)
        driver.execute_script("window.scrollBy(0, 500);")
        log_step(module, "Scrolled down the page", "Pass")
        time.sleep(3)
        game = driver.find_element(By.XPATH, "//span[contains(text(), 'God of War Ragnorok')]")
        game.click()
        log_step(module, "Clicked on 'God of War Ragnorok'", "Pass")
        time.sleep(5)
        add_to_cart_button = driver.find_element(By.ID, "add-to-cart-button")
        add_to_cart_button.click()
        log_step(module, "Clicked 'Add to Cart' button", "Pass")
        time.sleep(5)
    except Exception as e:
        log_step(module, f"Error: {e}", "Fail")
    finally:
        driver.quit()
