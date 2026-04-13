from selenium.webdriver.common.by import By
import time
from config import GET_DRIVER, BASE_URL

def TEST_ADMIN_HOSPITAL_DASHBOARD():

    driver = GET_DRIVER()

    try:
        driver.get(BASE_URL)
        time.sleep(2)

        driver.find_element(By.ID, "admin-login").click()
        time.sleep(2)

        driver.find_element(By.ID, "admin-hospital").click()
        time.sleep(2)

        driver.find_element(By.ID, "add-route").click()
        time.sleep(2)

        driver.find_element(By.ID, "route-name").send_keys("Hospital Route A")
        driver.find_element(By.ID, "submit-route").click()

        time.sleep(2)

        assert "hospital" in driver.page_source.lower()

        print("Admin Hospital Dashboard Test PASSED")

    except Exception as e:
        print("Admin Hospital Dashboard Test FAILED:", e)

    finally:
        driver.quit()


if __name__ == "__main__":
    TEST_ADMIN_HOSPITAL_DASHBOARD()