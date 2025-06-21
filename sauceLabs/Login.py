from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Edge driver
driver = webdriver.Edge()

# Open SauceDemo login page
driver.get("https://www.saucedemo.com/")

# Maximize the browser window
driver.maximize_window()

# Locate the username and password fields and enter credentials
username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")

username.send_keys("standard_user")
password.send_keys("secret_sauce")

# Click the login button
login_button = driver.find_element(By.XPATH, "//input[@type='submit']")
login_button.click()

# Wait for a few seconds to ensure the page loads
time.sleep(3)

# Verify successful login by checking the URL
assert "inventory.html" in driver.current_url

print("Test passed: Login successfully")

# Close the browser
driver.quit()
