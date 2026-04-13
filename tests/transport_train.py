from selenium.webdriver.common.by import By
import time
from config import GET_DRIVER, BASE_URL

def TEST_ADMIN_TRAIN_DASHBOARD():

    driver = GET_DRIVER()

    try:
        driver.get(BASE_URL)
        time.sleep(2)

        driver.find_element(By.ID, "admin-login").click()
        time.sleep(2)

        driver.find_element(By.ID, "admin-train").click()
        time.sleep(2)

        driver.find_element(By.ID, "add-route").click()
        time.sleep(2)

        driver.find_element(By.ID, "route-name").send_keys("Train Route A")
        driver.find_element(By.ID, "submit-route").click()

        time.sleep(2)

        assert "train" in driver.page_source.lower()

        print("Admin Train Dashboard Test PASSED")

    except Exception as e:
        print("Admin Train Dashboard Test FAILED:", e)

    finally:
        driver.quit()


if __name__ == "__main__":
    TEST_ADMIN_TRAIN_DASHBOARD()