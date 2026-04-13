from selenium.webdriver.common.by import By
import time
from config import GET_DRIVER, BASE_URL

def TEST_HOUSING_FACILITY():

    driver = GET_DRIVER()

    try:
        driver.get(BASE_URL)
        time.sleep(2)

        housing_btn = driver.find_element(By.ID, "housing")
        housing_btn.click()

        time.sleep(2)

        assert "housing" in driver.current_url.lower() or "housing" in driver.page_source.lower()

        print("Housing Facility Test PASSED")

    except Exception as e:
        print("Housing Facility Test FAILED:", e)

    finally:
        driver.quit()


if __name__ == "__main__":
    TEST_HOUSING_FACILITY()