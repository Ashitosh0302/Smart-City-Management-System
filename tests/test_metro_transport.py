from selenium.webdriver.common.by import By
import time
from config import GET_DRIVER, BASE_URL

def TEST_METRO_SERVICE():

    driver = GET_DRIVER()

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