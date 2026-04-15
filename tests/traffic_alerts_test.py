from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def TEST_TRAFFIC_ALERTS():
    PORT = "3070"
    LOGIN_URL = f"http://localhost:{PORT}/login"
    DASHBOARD_URL = f"http://localhost:{PORT}/citizen/alerts/traffic"

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

if __name__ == "__main__":
    TEST_TRAFFIC_ALERTS()
