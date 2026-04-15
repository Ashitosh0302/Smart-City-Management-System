from selenium.webdriver.common.by import By
import time
from config import GET_DRIVER, BASE_URL

def TEST_POLICE_SERVICE():
    
    driver = GET_DRIVER()

    try:
        driver.get(BASE_URL)
        time.sleep(2)

        police_btn = driver.find_element(By.ID, "police")
        police_btn.click()

        time.sleep(2)

        assert "police" in driver.current_url.lower() or "police" in driver.page_source.lower()

        print("Police Service Test PASSED")

    except Exception as e:
        print("Police Service Test FAILED:", e)

    finally:
        driver.quit()


if __name__ == "__main__":
    TEST_POLICE_SERVICE()
