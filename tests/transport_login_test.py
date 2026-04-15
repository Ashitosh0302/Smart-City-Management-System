from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def TEST_TRANSPORT_LOGIN():
    PORT = "3070"
    URL = f"http://localhost:{PORT}/login"

    edge_options = Options()
    edge_options.add_argument("--headless")
    edge_options.add_argument("--no-sandbox")
    edge_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=edge_options)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get(URL)
        time.sleep(2)

        # ✅ Step 1: Click "Authority"
        driver.find_element(By.XPATH, "//*[text()='Authority']").click()
        time.sleep(1)

        # ✅ Step 2: Select "Transport"
        driver.find_element(By.XPATH, "//*[text()='Transport']").click()
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
            print("✅ Transport authority login successful")
        else:
            print("❌ Transport authority login failed")

    except Exception as e:
        print("❌ Error during transport login:", e)

    finally:
        driver.quit()

if __name__ == "__main__":
    TEST_TRANSPORT_LOGIN()
