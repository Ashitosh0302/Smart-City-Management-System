from selenium.webdriver.common.by import By
import time
from config import GET_DRIVER, BASE_URL

def TEST_PARK_FACILITY():

    driver = GET_DRIVER()

    try:
        driver.get(BASE_URL)
        time.sleep(2)

        park_btn = driver.find_element(By.ID, "park")
        park_btn.click()

        time.sleep(2)

        assert "park" in driver.current_url.lower() or "park" in driver.page_source.lower()

        print("Park Facility Test PASSED")

    except Exception as e:
        print("Park Facility Test FAILED:", e)

    finally:
        driver.quit()


if __name__ == "__main__":
    TEST_PARK_FACILITY()