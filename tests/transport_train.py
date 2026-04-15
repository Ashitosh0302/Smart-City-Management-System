from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def TEST_ADMIN_TRAIN_DASHBOARD():
    PORT = "3070"

    edge_options = Options()
    edge_options.add_argument("--headless")
    edge_options.add_argument("--no-sandbox")
    edge_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=edge_options)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get(BASE_URL)
        time.sleep(2)

        driver.find_element(By.ID, "admin-login").click()
        time.sleep(2)

        driver.find_element(By.ID, "admin-train").click()
        time.sleep(2)

        driver.find_element(By.ID, "add-route").click()
        time.sleep(2)

        driver.find_element(By.ID, "route-name").send_keys("Train Route A")
        driver.find_element(By.ID, "submit-route").click()

        time.sleep(2)

        assert "train" in driver.page_source.lower()

        print("Admin Train Dashboard Test PASSED")

    except Exception as e:
        print("Admin Train Dashboard Test FAILED:", e)

    finally:
        driver.quit()

if __name__ == "__main__":
    TEST_ADMIN_TRAIN_DASHBOARD()
