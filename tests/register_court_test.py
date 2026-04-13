from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import random


def TEST_COURT_REGISTRATION():
    
    PORT = "3070"
    URL = f"http://localhost:{PORT}/court/court_register"   # change if needed
    
    service = Service("chromedriver")  # update path if needed
    driver = webdriver.Chrome()
    driver.maximize_window()

    # ✅ Dynamic Data (to avoid duplicate emails)
    rand = random.randint(1000, 9999)

    court_data = {
        "email": f"court{rand}@gmail.com",
        "password": "Court@123",
        "confirm_password": "Court@123"
    }

    try:
        driver.get(URL)
        time.sleep(2)

        # ✅ Fill Form (update locators if needed)
        driver.find_element(By.NAME, "email").send_keys(court_data["email"])
        driver.find_element(By.NAME, "password").send_keys(court_data["password"])
        driver.find_element(By.NAME, "confirm_password").send_keys(court_data["confirm_password"])

        # ✅ Submit Form
        driver.find_element(By.TAG_NAME, "button").click()
        time.sleep(3)

        # ✅ Check Result
        current_url = driver.current_url
        page_text = driver.find_element(By.TAG_NAME, "body").text

        if "login" in current_url.lower() or "success" in page_text.lower():
            print("✅ Court authority registration successful")
        else:
            print("❌ Registration may have failed")

    except Exception as e:
        print("❌ Error during court registration:", e)

    finally:
        driver.quit()


if __name__ == "__main__":
    TEST_COURT_REGISTRATION()
