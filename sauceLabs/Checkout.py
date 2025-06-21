from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_checkout_process():
    # Initialize Edge WebDriver
    driver = webdriver.Edge()

    try:
        # 1. Login to SauceDemo
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # 2. Add product to cart
        driver.find_element(By.XPATH, "//button[contains(@id,'add-to-cart')]").click()

        # 3. Go to cart
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # 4. Proceed to checkout
        driver.find_element(By.ID, "checkout").click()

        # 5. Fill checkout information
        driver.find_element(By.ID, "first-name").send_keys("John")
        driver.find_element(By.ID, "last-name").send_keys("Doe")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        driver.find_element(By.ID, "continue").click()

        # 6. Complete checkout
        driver.find_element(By.ID, "finish").click()

        # 7. Verify order completion
        confirmation = driver.find_element(By.CLASS_NAME, "complete-header")
        assert confirmation.text == "Thank you for your order!"
        print("Test passed: Checkout completed successfully")

    except Exception as e:
        print(f"Test failed: {str(e)}")
    finally:
        # Close the browser
        time.sleep(2)  # Visual confirmation
        driver.quit()


if __name__ == "__main__":
    test_checkout_process()
