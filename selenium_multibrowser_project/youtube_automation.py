from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

def run_youtube_flow():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.youtube.com")
    try:
        time.sleep(5)
        search_box = driver.find_element(By.NAME, "search_query")
        search_box.send_keys("selenium freecodecamp")
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)
        video = driver.find_element(By.XPATH, "//a[contains(@title, 'Selenium') and contains(@href, 'watch')]")
        video.click()
        time.sleep(5)
        driver.refresh()
        time.sleep(5)
        driver.back()
        time.sleep(5)   
        driver.forward()
        time.sleep(5)
    except Exception as e:
        print("YouTube Error:", e)
        driver.save_screenshot("youtube_error.png")
    finally:
        driver.quit()
