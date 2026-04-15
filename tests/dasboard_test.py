from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def TEST_HOME_PAGE():
    
    PORT = "3070"
    BASE_URL = f"http://localhost:{PORT}/"
    
    driver = webdriver.Chrome()   #  FIXED

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