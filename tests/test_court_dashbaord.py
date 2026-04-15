from selenium.webdriver.common.by import By
import time
from config import GET_DRIVER, BASE_URL

def TEST_ADMIN_COURT_DASHBOARD():

    driver = GET_DRIVER()

    try:
        driver.get(BASE_URL)
        time.sleep(2)

        # login (if required)
        driver.find_element(By.ID, "admin-login").click()
        time.sleep(2)

        # open admin court dashboard
        driver.find_element(By.ID, "admin-court").click()
        time.sleep(2)

        # open add route form
        driver.find_element(By.ID, "add-route").click()
        time.sleep(2)

        # fill route data
        driver.find_element(By.ID, "route-name").send_keys("Court Route A")
        driver.find_element(By.ID, "submit-route").click()

        time.sleep(2)

        assert "court" in driver.page_source.lower()

        print("Admin Court Dashboard Test PASSED")

    except Exception as e:
        print("Admin Court Dashboard Test FAILED:", e)

    finally:
        driver.quit()


if __name__ == "__main__":
    TEST_ADMIN_COURT_DASHBOARD()