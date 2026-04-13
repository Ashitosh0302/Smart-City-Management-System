from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


def LOGIN_TEST(user_input, password):

    PORT = "5000"
    URL = f"http://localhost:{PORT}/login"

    service = Service("chromedriver")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    try:
        driver.get(URL)
        time.sleep(2)

        # ✅ Click Authority
        driver.find_element(By.XPATH, "//*[text()='Authority']").click()
        time.sleep(1)

        # ✅ Select Government
        driver.find_element(By.XPATH, "//*[text()='Government']").click()
        time.sleep(1)

        # ✅ Enter Email / Username
        driver.find_element(By.NAME, "email").send_keys(user_input)

        # ✅ Enter Password
        driver.find_element(By.NAME, "password").send_keys(password)

        # ✅ Click Login
        driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
        time.sleep(3)

        # ✅ Check result
        if "dashboard" in driver.current_url.lower():
            print(f"✅ Login successful with: {user_input}")
        else:
            print(f"❌ Login failed with: {user_input}")

    except Exception as e:
        print("❌ Error:", e)

    finally:
        driver.quit()


if __name__ == "__main__":

    # 🔹 Test with USERNAME
    LOGIN_TEST("govuser1", "Gov@123")

    # 🔹 Test with EMAIL
    LOGIN_TEST("govuser1@gmail.com", "Gov@123")
