from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


def TEST_GOV_LOGIN():
    
    PORT = "5000"
    URL = f"http://localhost:{PORT}/login"
    
    service = Service("chromedriver")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    login_data = {
        "user": "govuser1",   # or email
        "password": "Gov@123"
    }

    try:
        driver.get(URL)
        time.sleep(2)

        # ✅ Step 1: Click "Authority"
        driver.find_element(By.XPATH, "//div[contains(text(),'Authority')]").click()
        time.sleep(1)

        # ✅ Step 2: Select "Government" department
        driver.find_element(By.XPATH, "//div[contains(text(),'Government')]").click()
        time.sleep(1)

        # ✅ Step 3: Enter Email / Username
        driver.find_element(By.NAME, "email").send_keys(login_data["user"])

        # ✅ Step 4: Enter Password
        driver.find_element(By.NAME, "password").send_keys(login_data["password"])

        # ✅ Step 5: Click Login Button
        driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
        time.sleep(3)

        # ✅ Check Success
        if "dashboard" in driver.current_url.lower():
            print("✅ Government login successful")
        else:
            print("❌ Government login failed")

    except Exception as e:
        print("❌ Error:", e)

    finally:
        driver.quit()


if __name__ == "__main__":
    TEST_GOV_LOGIN()
