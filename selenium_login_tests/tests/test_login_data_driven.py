import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
@pytest.fixture
def setup():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
def test_valid_credentials_login(setup):
    driver = setup
    valid_username = "standard_user"
    valid_password = "secret_sauce"
    
    driver.find_element(By.ID, "user-name").clear()
    driver.find_element(By.ID, "user-name").send_keys(valid_username)
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys(valid_password)
    driver.find_element(By.ID, "login-button").click()
    
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".title")))
        is_logged_in = True
    except TimeoutException:
        is_logged_in = False
    
    try:
        error_element = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
        error_msg = error_element.text
    except NoSuchElementException:
        error_msg = None
    
    assert is_logged_in, "Login should be successful with valid credentials"
    assert error_msg is None, "No error message should be displayed"
    print("Valid credentials test PASSED")

def test_invalid_username_login(setup):
    driver = setup
    invalid_username = "invalid_user"
    valid_password = "secret_sauce"
    
    driver.find_element(By.ID, "user-name").clear()
    driver.find_element(By.ID, "user-name").send_keys(invalid_username)
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys(valid_password)
    driver.find_element(By.ID, "login-button").click()
    
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".title")))
        is_logged_in = True
    except TimeoutException:
        is_logged_in = False
    
    try:
        error_element = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
        error_msg = error_element.text
    except NoSuchElementException:
        error_msg = None
    
    assert not is_logged_in, "Login should fail with invalid username"
    assert error_msg is not None, "Error message should be displayed"
    assert "Username and password do not match" in error_msg, f"Expected authentication error, got: {error_msg}"
    print("Invalid username test PASSED")

def test_invalid_password_login(setup):
    driver = setup
    valid_username = "standard_user"
    invalid_password = "wrong_password"
    
    driver.find_element(By.ID, "user-name").clear()
    driver.find_element(By.ID, "user-name").send_keys(valid_username)
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys(invalid_password)
    driver.find_element(By.ID, "login-button").click()
    
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".title")))
        is_logged_in = True
    except TimeoutException:
        is_logged_in = False
    
    try:
        error_element = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
        error_msg = error_element.text
    except NoSuchElementException:
        error_msg = None
    
    assert not is_logged_in, "Login should fail with invalid password"
    assert error_msg is not None, "Error message should be displayed"
    assert "Username and password do not match" in error_msg, f"Expected authentication error, got: {error_msg}"
    print(" Invalid password test PASSED")

def test_empty_username_login(setup):
    driver = setup
    empty_username = ""
    valid_password = "secret_sauce"
    
    driver.find_element(By.ID, "user-name").clear()
    driver.find_element(By.ID, "user-name").send_keys(empty_username)
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys(valid_password)
    driver.find_element(By.ID, "login-button").click()
    
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".title")))
        is_logged_in = True
    except TimeoutException:
        is_logged_in = False
    try:
        error_element = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
        error_msg = error_element.text
    except NoSuchElementException:
        error_msg = None
    assert not is_logged_in, "Login should fail with empty username"
    assert error_msg is not None, "Error message should be displayed"
    assert "Username is required" in error_msg, f"Expected username required error, got: {error_msg}"
    print("Empty username test PASSED")

def test_empty_password_login(setup):
    driver = setup
    valid_username = "standard_user"
    empty_password = ""
    driver.find_element(By.ID, "user-name").clear()
    driver.find_element(By.ID, "user-name").send_keys(valid_username)
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys(empty_password)
    driver.find_element(By.ID, "login-button").click()
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".title")))
        is_logged_in = True
    except TimeoutException:
        is_logged_in = False
    try:
        error_element = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
        error_msg = error_element.text
    except NoSuchElementException:
        error_msg = None
    
    assert not is_logged_in, "Login should fail with empty password"
    assert error_msg is not None, "Error message should be displayed"
    assert "Password is required" in error_msg, f"Expected password required error, got: {error_msg}"
    print("Empty password test PASSED")
def test_both_fields_empty_login(setup):
    driver = setup
    empty_username = ""
    empty_password = ""
    
    driver.find_element(By.ID, "user-name").clear()
    driver.find_element(By.ID, "user-name").send_keys(empty_username)
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys(empty_password)
    driver.find_element(By.ID, "login-button").click()
    
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".title")))
        is_logged_in = True
    except TimeoutException:
        is_logged_in = False
    
    try:
        error_element = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
        error_msg = error_element.text
    except NoSuchElementException:
        error_msg = None
    
    assert not is_logged_in, "Login should fail with both fields empty"
    assert error_msg is not None, "Error message should be displayed"
    assert "Username is required" in error_msg, f"Expected username required error, got: {error_msg}"
    print("Both fields empty test PASSED")

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])