from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_add_to_cart():
    # Initialize Edge WebDriver
    driver = webdriver.Edge()

    try:
        # 1. Login to SauceDemo
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Verify login success
        assert "inventory.html" in driver.current_url

        # 2. Add first product to cart
        add_to_cart_button = driver.find_element(By.XPATH, "//button[contains(@id,'add-to-cart')]")
        product_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        add_to_cart_button.click()

        # 3. Verify item was added to cart
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert cart_badge.text == "1"

        # 4. Go to cart and verify product is there
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        cart_item = driver.find_element(By.CLASS_NAME, "inventory_item_name")
        assert cart_item.text == product_name

        print("Test passed: Product successfully added to cart")

    except Exception as e:
        print(f"Test failed: {str(e)}")
    finally:
        # Close the browser
        time.sleep(2)  # Just for visual confirmation
        driver.quit()


if __name__ == "__main__":
    test_add_to_cart()
