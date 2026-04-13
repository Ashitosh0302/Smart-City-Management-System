from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def TEST_CITIZEN_DASHBOARD():

    PORT = "3070"
    LOGIN_URL = f"http://localhost:{PORT}/login"
    DASHBOARD_URL = f"http://localhost:{PORT}/citizen"

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.set_window_size(1920, 1080)

    wait = WebDriverWait(driver, 15)

    # ✅ Test Data
    login_data = {
        "user": "testuser1",   # OR email
        "password": "Test@123"
    }

    try:
        # ===============================
        # 🔹 STEP 1: Open Login Page
        # ===============================
        driver.get(LOGIN_URL)

        # ===============================
        # 🔹 STEP 2: Enter Username/Email
        # ===============================
        email_input = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
        email_input.clear()
        email_input.send_keys(login_data["user"])

        # ===============================
        # 🔹 STEP 3: Enter Password
        # ===============================
        password_input = driver.find_element(By.NAME, "password")
        password_input.clear()
        password_input.send_keys(login_data["password"])

        # ===============================
        # 🔹 STEP 4: Click Login
        # ===============================
        login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        driver.execute_script("arguments[0].click();", login_btn)

        # ===============================
        # 🔹 STEP 5: Wait for Login Success
        # ===============================
        wait.until(lambda d: "login" not in d.current_url.lower())

        # ===============================
        # 🔹 STEP 6: Open Dashboard
        # ===============================
        driver.get(DASHBOARD_URL)

        # ===============================
        # 🔹 STEP 7: Validate Dashboard
        # ===============================
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        current_url = driver.current_url.lower()
        page_text = driver.find_element(By.TAG_NAME, "body").text.lower()

        if "citizen" in current_url or "dashboard" in page_text or "welcome" in page_text:
            print("✅ Citizen dashboard loaded successfully")
        else:
            print("❌ Dashboard not loaded properly")

    except Exception as e:
        print("❌ Error during dashboard test:", e)

    finally:
        driver.quit()


if __name__ == "__main__":
    TEST_CITIZEN_DASHBOARD()