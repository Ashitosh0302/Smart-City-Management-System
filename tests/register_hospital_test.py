from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def TEST_HOSPITAL_REGISTRATION():
    PORT = "3070"
    URL = f"http://localhost:{PORT}/hospital/hospital_register"

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

        # ✅ Fill Form (update if your field names differ)
        driver.find_element(By.NAME, "email").send_keys(hospital_data["email"])
        driver.find_element(By.NAME, "password").send_keys(hospital_data["password"])
        driver.find_element(By.NAME, "confirm_password").send_keys(hospital_data["confirm_password"])

        # ✅ Submit Form
        driver.find_element(By.TAG_NAME, "button").click()
        time.sleep(3)

        # ✅ Check Result
        current_url = driver.current_url
        page_text = driver.find_element(By.TAG_NAME, "body").text

        if "login" in current_url.lower() or "success" in page_text.lower():
            print("✅ Hospital authority registration successful")
        else:
            print("❌ Registration may have failed")

    except Exception as e:
        print("❌ Error during hospital registration:", e)

    finally:
        driver.quit()

if __name__ == "__main__":
    TEST_HOSPITAL_REGISTRATION()
