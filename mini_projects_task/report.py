from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.google.com")
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium")
search_box.send_keys(Keys.RETURN)

html = """
<html>
<head><title>Simple Report</title></head>
<body>
<h2>Google Search Test</h2>
<p>Searched for: <b>Selenium</b></p>
<p>Page Title: {}</p>
</body>
</html>
""".format(driver.title)
with open("simple_report.html", "w", encoding="utf-8") as f:
    f.write(html)
driver.quit()
print("✅ Report saved as simple_report.html")
