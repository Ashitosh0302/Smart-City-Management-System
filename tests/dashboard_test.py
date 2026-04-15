from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def TEST_HOME_PAGE():
    PORT = "3070"
    BASE_URL = f"http://localhost:{PORT}/"

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

        print("Page Title:", driver.title)

        assert driver.current_url == BASE_URL

        body = driver.find_element(By.TAG_NAME, "body")
        assert body is not None

        print("✅ Home page loaded successfully")

    except Exception as e:
        print("❌ Test Failed:", str(e))

    finally:
        driver.quit()

if __name__ == "__main__":
    TEST_HOME_PAGE()
