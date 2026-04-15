from selenium.webdriver.common.by import By
import time
from config import GET_DRIVER, BASE_URL

def TEST_FIRE_SERVICE():
    
    driver = GET_DRIVER()

    try:
        driver.get(BASE_URL)
        time.sleep(2)

        fire_btn = driver.find_element(By.ID, "fire")
        fire_btn.click()

        time.sleep(2)

        assert "fire" in driver.current_url.lower() or "fire" in driver.page_source.lower()

        print("Fire Service Test PASSED")

    except Exception as e:
        print("Fire Service Test FAILED:", e)

    finally:
        driver.quit()


if __name__ == "__main__":
    TEST_FIRE_SERVICE()
