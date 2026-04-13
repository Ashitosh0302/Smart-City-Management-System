from selenium.webdriver.common.by import By
import time
from config import GET_DRIVER, BASE_URL

def TEST_BUS_SERVICE():

    driver = GET_DRIVER()

    try:
        driver.get(BASE_URL)
        time.sleep(2)

        bus_btn = driver.find_element(By.ID, "bus")
        bus_btn.click()

        time.sleep(2)

        assert "bus" in driver.current_url.lower() or "bus" in driver.page_source.lower()

        print("Bus Service Test PASSED")

    except Exception as e:
        print("Bus Service Test FAILED:", e)

    finally:
        driver.quit()


if __name__ == "__main__":
    TEST_BUS_SERVICE()