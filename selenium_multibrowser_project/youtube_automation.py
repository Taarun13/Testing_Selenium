from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from logger import log_step

def run_youtube_flow():
    module = "YouTube"
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.youtube.com")

    try:
        log_step(module, "Opened YouTube homepage", "Pass")
        time.sleep(5)
        search_box = driver.find_element(By.NAME, "search_query")
        log_step(module, "Located search box", "Pass")
        search_box.send_keys("selenium freecodecamp")
        log_step(module, "Entered search query 'selenium freecodecamp'", "Pass")
        search_box.send_keys(Keys.RETURN)
        log_step(module, "Submitted search", "Pass")
        time.sleep(3)
        video = driver.find_element(By.XPATH, "//a[contains(@title, 'Selenium') and contains(@href, 'watch')]")
        video.click()
        log_step(module, "Clicked on first Selenium video", "Pass")
        time.sleep(5)
        driver.refresh()
        log_step(module, "Refreshed the page", "Pass")
        time.sleep(5)
        try:
            driver.back()
            log_step(module, "Went back to previous page", "Pass")
        except Exception as e:
            log_step(module, f"Failed navigating back: {e}", "Fail")
        time.sleep(5)
        try:
            driver.forward()
            log_step(module, "Went forward to next page", "Pass")
        except Exception as e:
            log_step(module, f"Failed navigating forward: {e}", "Fail")
        time.sleep(5)
    except Exception as e:
        log_step(module, f"Error: {e}", "Fail")
    finally:
        driver.quit()
