from selenium.webdriver.common.by import By
import time
from config import GET_DRIVER, BASE_URL

def TEST_TRAIN_SERVICE():

    driver = GET_DRIVER()

    try:
        driver.get(BASE_URL)
        time.sleep(2)

        train_btn = driver.find_element(By.ID, "train")
        train_btn.click()

        time.sleep(2)

        assert "train" in driver.current_url.lower() or "train" in driver.page_source.lower()

        print("Train Service Test PASSED")

    except Exception as e:
        print("Train Service Test FAILED:", e)

    finally:
        driver.quit()


if __name__ == "__main__":
    TEST_TRAIN_SERVICE()