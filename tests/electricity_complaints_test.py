from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


def TEST_ELECTRICITY_COMPLAINT_FULL():

    PORT = "3070"
    LOGIN_URL = f"http://localhost:{PORT}/login"
    ELECTRICITY_URL = f"http://localhost:{PORT}/citizen/complaints/electricity"

    service = Service("chromedriver")
    driver = webdriver.Chrome()
    driver.maximize_window()

    # ✅ Login Data
    login_data = {
        "user": "testuser1",
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

        # 🔹 Step 2: Open Electricity Complaint Page
        driver.get(ELECTRICITY_URL)
        time.sleep(3)

        # ==========================
        # 🔹 CONSUMER DETAILS
        # ==========================
        driver.find_element(By.NAME, "consumer[fullName]").send_keys("Test User")
        driver.find_element(By.NAME, "consumer[serviceNumber]").send_keys("SRV12345")
        driver.find_element(By.NAME, "consumer[meterNumber]").send_keys("MTR98765")
        driver.find_element(By.NAME, "consumer[phone]").send_keys("9876543210")
        driver.find_element(By.NAME, "consumer[email]").send_keys("testuser@gmail.com")

        # ==========================
        # 🔹 CONNECTION TYPE (card click)
        # ==========================
        driver.find_element(By.XPATH, "//div[contains(text(),'Commercial')]").click()
        time.sleep(1)

        # ==========================
        # 🔹 PROVIDER (card click)
        # ==========================
        driver.find_element(By.XPATH, "//div[contains(text(),'BESCOM')]").click()
        time.sleep(1)

        # ==========================
        # 🔹 ADDRESS DETAILS
        # ==========================
        driver.find_element(By.NAME, "address[addressLine]").send_keys(
            "House 101, MG Road"
        )
        driver.find_element(By.NAME, "address[landmark]").send_keys("Near Temple")
        driver.find_element(By.NAME, "address[area]").send_keys("City Center")
        driver.find_element(By.NAME, "address[city]").send_keys("Ahmedabad")

        driver.find_element(By.NAME, "address[ward]").send_keys("Ward 1")

        # ==========================
        # 🔹 ISSUE TYPE (card click)
        # ==========================
        driver.find_element(By.XPATH, "//div[contains(text(),'Power Cut')]").click()
        time.sleep(1)

        # ==========================
        # 🔹 ISSUE DATE & TIME
        # ==========================
        driver.find_element(By.NAME, "issue[issueDate]").send_keys("2026-04-13")
        driver.find_element(By.NAME, "issue[issueTime]").send_keys("10:30")

        # ==========================
        # 🔹 DURATION
        # ==========================
        driver.find_element(By.NAME, "issue[duration]").send_keys("1_4_hours")

        # ==========================
        # 🔹 DESCRIPTION
        # ==========================
        driver.find_element(By.NAME, "issue[description]").send_keys(
            "Power cut in our area since morning. No electricity."
        )

        # ==========================
        # 🔹 SUBMIT FORM
        # ==========================
        driver.find_element(By.ID, "submitBtn").click()
        time.sleep(5)

        # ==========================
        # 🔹 CHECK SUCCESS MODAL
        # ==========================
        try:
            modal = driver.find_element(By.ID, "successModal")

            if modal.is_displayed():
                print("✅ Electricity complaint submitted successfully")
            else:
                print("❌ Submission failed")

        except:
            print("❌ Success modal not found")

    except Exception as e:
        print("❌ Error:", e)

    finally:
        driver.quit()

if __name__ == "__main__":
    TEST_ELECTRICITY_COMPLAINT_FULL()
