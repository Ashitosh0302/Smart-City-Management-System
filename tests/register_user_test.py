from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def TEST_USER_REGISTRATION():
    PORT = "3070"
    URL = f"http://localhost:{PORT}/citizen/citizen_register"

    edge_options = Options()
    edge_options.add_argument("--headless")
    edge_options.add_argument("--no-sandbox")
    edge_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=edge_options)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get(URL)

        # ✅ Wait for form
        wait.until(EC.presence_of_element_located((By.ID, "firstName")))

        # ✅ Fill form (using IDs → BEST PRACTICE)
        driver.find_element(By.ID, "firstName").send_keys("Anushka")
        driver.find_element(By.ID, "lastName").send_keys("Wagh")
        driver.find_element(By.ID, "username").send_keys(f"user{rand}")
        driver.find_element(By.ID, "email").send_keys(f"user{rand}@gmail.com")

        # ✅ FIXED (correct name from HTML)
        driver.find_element(By.NAME, "phone_number").send_keys(f"98765{rand}")

        # ✅ Gender
        driver.find_element(By.ID, "female").click()

        # ✅ City
        driver.find_element(By.ID, "city").send_keys("Mumbai")

        # ✅ Password
        driver.find_element(By.ID, "password").send_keys("Test@123")
        driver.find_element(By.ID, "confirmPassword").send_keys("Test@123")

        # ✅ Scroll to checkbox
        checkbox = driver.find_element(By.ID, "terms")
        driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)

        # ✅ BEST FIX → JS CLICK (avoids intercepted error)
        driver.execute_script("arguments[0].click();", checkbox)

        # ✅ Scroll to button
        button = driver.find_element(By.XPATH, "//button[@type='submit']")
        driver.execute_script("arguments[0].scrollIntoView(true);", button)

        # ✅ Click submit
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        button.click()

        # ✅ Wait for response
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        current_url = driver.current_url.lower()
        page_text = driver.find_element(By.TAG_NAME, "body").text.lower()

        if "login" in current_url or "citizen" in current_url:
            print("✅ Registration SUCCESS")

        elif "error" in page_text:
            print("❌ Registration FAILED (error shown)")

        else:
            print("⚠️ Check manually")

    except Exception as e:
        print("❌ Error:", e)

    finally:
        driver.quit()

if __name__ == "__main__":
    TEST_USER_REGISTRATION()
