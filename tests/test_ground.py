from selenium.webdriver.common.by import By
import time
from config import GET_DRIVER, BASE_URL

def TEST_GROUND_FACILITY():

    driver = GET_DRIVER()

    try:
        driver.get(BASE_URL)
        time.sleep(2)

        ground_btn = driver.find_element(By.ID, "ground")
        ground_btn.click()

        time.sleep(2)

        assert "ground" in driver.current_url.lower() or "ground" in driver.page_source.lower()

        print("Ground Facility Test PASSED")

    except Exception as e:
        print("Ground Facility Test FAILED:", e)

    finally:
        driver.quit()


if __name__ == "__main__":
    TEST_GROUND_FACILITY()