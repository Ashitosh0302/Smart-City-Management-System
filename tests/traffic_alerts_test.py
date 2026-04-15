from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


def TEST_TRAFFIC_ALERTS():
    
    PORT = "3070"
    LOGIN_URL = f"http://localhost:{PORT}/login"
    DASHBOARD_URL = f"http://localhost:{PORT}/citizen/alerts/traffic"

    service = Service("chromedriver")
    driver = webdriver.Chrome()
    driver.maximize_window()

    # ✅ Test Data (existing user)
    login_data = {
        "user": "testuser1",   # OR email
        "password": "Test@123"
    }

    try:
        # 🔹 Step 1: Login
        driver.get(LOGIN_URL)
        time.sleep(2)

        driver.find_element(By.NAME, "email").send_keys(login_data["user"])
        driver.find_element(By.NAME, "password").send_keys(login_data["password"])
        driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
        time.sleep(3)

        # 🔹 Step 2: Open Dashboard
        driver.get(DASHBOARD_URL)
        time.sleep(2)

        # 🔹 Step 3: Check Traffic Alerts Section
        page_text = driver.find_element(By.TAG_NAME, "body").text

        if "traffic" in page_text.lower():
            print("✅ Traffic Alerts section is visible")
        else:
            print("❌ Traffic Alerts not found")

        # 🔹 Step 4 (Optional): Click Traffic Alerts
        # (use if there is a button/link)
        try:
            driver.find_element(By.XPATH, "//*[contains(text(),'Traffic')]").click()
            time.sleep(2)
            print("✅ Traffic Alerts page opened")
        except:
            print("ℹ️ No clickable Traffic Alerts button found")

    except Exception as e:
        print("❌ Error during traffic alerts test:", e)

    finally:
        driver.quit()

<<<<<<< HEAD
=======

>>>>>>> 61c3cc00a000f2204436b07de06d74944b8999ba
if __name__ == "__main__":
    TEST_TRAFFIC_ALERTS()
