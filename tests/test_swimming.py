from selenium.webdriver.common.by import By
import time
from config import GET_DRIVER, BASE_URL

def TEST_SWIMMING_FACILITY():

    driver = GET_DRIVER()

    try:
        driver.get(BASE_URL)
        time.sleep(2)

        swimming_btn = driver.find_element(By.ID, "swimming")
        swimming_btn.click()

        time.sleep(2)

        assert "swimming" in driver.current_url.lower() or "swimming" in driver.page_source.lower()

        print("Swimming Facility Test PASSED")

    except Exception as e:
        print("Swimming Facility Test FAILED:", e)

    finally:
        driver.quit()


if __name__ == "__main__":
    TEST_SWIMMING_FACILITY()
