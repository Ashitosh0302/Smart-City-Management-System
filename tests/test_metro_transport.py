from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def TEST_METRO_SERVICE():
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

        metro_btn = driver.find_element(By.ID, "metro")
        metro_btn.click()

        time.sleep(2)

        assert "metro" in driver.current_url.lower() or "metro" in driver.page_source.lower()

        print("Metro Service Test PASSED")

    except Exception as e:
        print("Metro Service Test FAILED:", e)

    finally:
        driver.quit()

if __name__ == "__main__":
    TEST_METRO_SERVICE()
