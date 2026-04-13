from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


def TEST_CITIZEN_DASHBOARD():
    
    PORT = "3070"
    LOGIN_URL = f"http://localhost:{PORT}/login"
    DASHBOARD_URL = f"http://localhost:{PORT}/citizen"

    service = Service("chromedriver")
    driver = webdriver.Chrome()
    driver.maximize_window()

    # ✅ Test Data (existing user)
    login_data = {
        "user": "testuser1",   # OR "testuser1@gmail.com"
        "password": "Test@123"
    }

    try:
        # 🔹 Step 1: Open login page
        driver.get(LOGIN_URL)
        time.sleep(2)

        # 🔹 Step 2: Enter Email/Username
        driver.find_element(By.NAME, "email").send_keys(login_data["user"])

        # 🔹 Step 3: Enter Password
        driver.find_element(By.NAME, "password").send_keys(login_data["password"])

        # 🔹 Step 4: Click Login
        driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
        time.sleep(3)

        # 🔹 Step 5: Open Dashboard
        driver.get(DASHBOARD_URL)
        time.sleep(2)

        # 🔹 Step 6: Check Dashboard Loaded
        page_text = driver.find_element(By.TAG_NAME, "body").text

        if "dashboard" in driver.current_url.lower() or "welcome" in page_text.lower():
            print("✅ Citizen dashboard loaded successfully")
        else:
            print("❌ Dashboard not loaded properly")

    except Exception as e:
        print("❌ Error during dashboard test:", e)

    finally:
        driver.quit()


if __name__ == "__main__":
    TEST_CITIZEN_DASHBOARD()
