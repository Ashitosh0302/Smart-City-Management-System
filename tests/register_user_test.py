from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time
import random


def TEST_USER_REGISTRATION():
    
    PORT = "5000"
    URL = f"http://localhost:{PORT}/register"
    
    service = Service("chromedriver")  # update path if needed
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    # ✅ Dynamic Test Data (avoids duplicate user error)
    rand = random.randint(1000, 9999)

    user_data = {
        "first_name": "Anushka",
        "last_name": "Wagh",
        "username": f"user{rand}",
        "email": f"user{rand}@gmail.com",
        "mobile": f"98765{rand}",
        "gender": "female",   # change if needed
        "city": "Mumbai",     # change if dropdown
        "password": "Test@123",
        "confirm_password": "Test@123"
    }

    try:
        driver.get(URL)
        time.sleep(2)

        # ✅ Fill Form Fields
        # ⚠️ Change locators based on your HTML

        driver.find_element(By.NAME, "first_name").send_keys(user_data["first_name"])
        driver.find_element(By.NAME, "last_name").send_keys(user_data["last_name"])
        driver.find_element(By.NAME, "username").send_keys(user_data["username"])
        driver.find_element(By.NAME, "email").send_keys(user_data["email"])
        driver.find_element(By.NAME, "mobile").send_keys(user_data["mobile"])

        # ✅ Gender (Radio Button)
        driver.find_element(By.XPATH, f"//input[@name='gender' and @value='{user_data['gender']}']").click()

        # ✅ City (Dropdown OR Input)
        try:
            Select(driver.find_element(By.NAME, "city")).select_by_visible_text(user_data["city"])
        except:
            driver.find_element(By.NAME, "city").send_keys(user_data["city"])

        # ✅ Password Fields
        driver.find_element(By.NAME, "password").send_keys(user_data["password"])
        driver.find_element(By.NAME, "confirm_password").send_keys(user_data["confirm_password"])

        # ✅ Submit Form
        driver.find_element(By.TAG_NAME, "button").click()
        time.sleep(3)

        # ✅ Check Result
        current_url = driver.current_url
        page_text = driver.find_element(By.TAG_NAME, "body").text

        if "login" in current_url.lower() or "success" in page_text.lower():
            print("✅ User registration successful")
        else:
            print("❌ Registration may have failed")

    except Exception as e:
        print("❌ Error during registration:", e)

    finally:
        driver.quit()


if __name__ == "__main__":
    TEST_USER_REGISTRATION()
