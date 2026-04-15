from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


def TEST_COURT_LOGIN():
    
    PORT = "3070"
    URL = f"http://localhost:{PORT}/login"

    service = Service("chromedriver")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    # ✅ Test Data
    login_data = {
        "user": "courtuser1",   # OR "courtuser1@gmail.com"
        "password": "Court@123"
    }

    try:
        driver.get(URL)
        time.sleep(2)

        # ✅ Step 1: Click "Authority"
        driver.find_element(By.XPATH, "//*[text()='Authority']").click()
        time.sleep(1)

        # ✅ Step 2: Select "Court"
        driver.find_element(By.XPATH, "//*[text()='Court']").click()
        time.sleep(1)

        # ✅ Step 3: Enter Email / Username
        driver.find_element(By.NAME, "email").send_keys(login_data["user"])

        # ✅ Step 4: Enter Password
        driver.find_element(By.NAME, "password").send_keys(login_data["password"])

        # ✅ Step 5: Click Login
        driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
        time.sleep(3)

        # ✅ Step 6: Check Success
        if "dashboard" in driver.current_url.lower():
            print("✅ Court authority login successful")
        else:
            print("❌ Court authority login failed")

    except Exception as e:
        print("❌ Error during court login:", e)

    finally:
        driver.quit()

if __name__ == "__main__":
    TEST_COURT_LOGIN()
