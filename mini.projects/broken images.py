from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
browser = webdriver.Firefox()
browser.get("https://the-internet.herokuapp.com/broken_images")
browser.maximize_window()

images = browser.find_elements(By.TAG_NAME, "img")
broken_images = []
for image in images:
    src = image.get_attribute("src")
    if src:
        try:
            response = requests.get(src)
            if response.status_code != 200:
                broken_images.append(src)
                print("Broken Image found")
        except Exception as e:
            broken_images.append(src)
            print(f"Error checking image: {src}")
if broken_images:
    print("List of broken images:")
    for broken_image in broken_images:
        print(broken_image)
else:
    print("No broken images found")
browser.quit()
