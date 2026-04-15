from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def TEST_WATER_COMPLAINT_FULL():
    PORT = "3070"
    LOGIN_URL = f"http://localhost:{PORT}/login"
    WATER_URL = f"http://localhost:{PORT}/citizen/complaints/water"

    edge_options = Options()
    edge_options.add_argument("--headless")
    edge_options.add_argument("--no-sandbox")
    edge_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=edge_options)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    try:
        # 🔹 Step 1: Login
        driver.get(LOGIN_URL)
        time.sleep(2)

        driver.find_element(By.NAME, "email").send_keys(login_data["user"])
        driver.find_element(By.NAME, "password").send_keys(login_data["password"])
        driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
        time.sleep(3)

        # 🔹 Step 2: Open Water Complaint Page
        driver.get(WATER_URL)
        time.sleep(3)

        # ==========================
        # 🔹 LOCATION DETAILS
        # ==========================
        driver.find_element(By.NAME, "address[houseNo]").send_keys("101")
        driver.find_element(By.NAME, "address[street]").send_keys("MG Road")

        Select(driver.find_element(By.NAME, "address[ward]")).select_by_visible_text("Ward 1")

        driver.find_element(By.NAME, "address[pincode]").send_keys("416701")
        driver.find_element(By.NAME, "address[landmark]").send_keys("Near Temple")

        # ==========================
        # 🔹 ISSUE TYPE (click card)
        # ==========================
        driver.find_element(By.XPATH, "//div[contains(text(),'Water Leakage')]").click()
        time.sleep(1)

        # ==========================
        # 🔹 DURATION
        # ==========================
        Select(driver.find_element(By.NAME, "duration")).select_by_visible_text("1-2 days")

        # ==========================
        # 🔹 DESCRIPTION
        # ==========================
        driver.find_element(By.NAME, "description").send_keys(
            "There is continuous water leakage in our street."
        )

        # ==========================
        # 🔹 DATE & TIME
        # ==========================
        driver.find_element(By.NAME, "issueDate").send_keys("2026-04-13")
        driver.find_element(By.NAME, "issueTime").send_keys("10:30")

        # ==========================
        # 🔹 CONTACT INFO
        # ==========================
        driver.find_element(By.NAME, "fullName").send_keys("Test User")
        driver.find_element(By.NAME, "phone").send_keys("9876543210")
        driver.find_element(By.NAME, "email").send_keys("testuser@gmail.com")

        # ==========================
        # 🔹 SUBMIT FORM
        # ==========================
        driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()
        time.sleep(5)

        # ==========================
        # 🔹 CHECK SUCCESS
        # ==========================
        try:
            success_modal = driver.find_element(By.ID, "successModal")

            if success_modal.is_displayed():
                print("✅ Water complaint submitted successfully")
            else:
                print("❌ Submission failed")

        except:
            print("❌ Success modal not found")

    except Exception as e:
        print("❌ Error:", e)

    finally:
        driver.quit()

if __name__ == "__main__":
    TEST_WATER_COMPLAINT_FULL()
