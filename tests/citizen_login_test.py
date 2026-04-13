from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


def TEST_USER_LOGIN():
    
    PORT = "5000"
    URL = f"http://localhost:{PORT}/login"   # change if needed
    
    service = Service("chromedriver")  # update path if needed
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    # ✅ Test Data (use existing registered user)
    login_data = {
        "user": "testuser1",   # OR "testuser1@gmail.com"
        "password": "Test@123"
    }

    try:
        driver.get(URL)
        time.sleep(2)

        # ✅ Enter Email / Username
        # ⚠️ Change locator based on your HTML

        driver.find_element(By.NAME, "email").send_keys(login_data["user"])
        # OR if your field is username:
        # driver.find_element(By.NAME, "username").send_keys(login_data["user"])

        # ✅ Enter Password
        driver.find_element(By.NAME, "password").send_keys(login_data["password"])

        # ✅ Click Login Button
        driver.find_element(By.TAG_NAME, "button").click()
        time.sleep(3)

        # ✅ Check Login Success
        if "dashboard" in driver.current_url.lower():
            print("✅ User (Citizen) login successful")
        else:
            print("❌ Login failed")

    except Exception as e:
        print("❌ Error during login:", e)

    finally:
        driver.quit()


if __name__ == "__main__":
    TEST_USER_LOGIN()
