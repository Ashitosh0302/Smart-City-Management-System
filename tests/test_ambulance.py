from selenium.webdriver.common.by import By
import time
from config import GET_DRIVER, BASE_URL

def TEST_AMBULANCE_SERVICE():
    
    driver = GET_DRIVER()

    try:
        driver.get(BASE_URL)
        time.sleep(2)

        ambulance_btn = driver.find_element(By.ID, "ambulance")
        ambulance_btn.click()

        time.sleep(2)

        assert "ambulance" in driver.current_url.lower() or "ambulance" in driver.page_source.lower()

        print("Ambulance Service Test PASSED")

    except Exception as e:
        print("Ambulance Service Test FAILED:", e)

    finally:
        driver.quit()


if __name__ == "__main__":
    TEST_AMBULANCE_SERVICE()
