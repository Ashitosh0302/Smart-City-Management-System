from selenium import webdriver
<<<<<<< HEAD
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def TEST_USER_LOGIN():
    PORT = "3070"
    URL = f"http://localhost:{PORT}/login"

    edge_options = Options()
    edge_options.add_argument("--headless")
    edge_options.add_argument("--no-sandbox")
    edge_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=edge_options)
    driver.maximize_window()
=======
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def TEST_USER_LOGIN():
    
    PORT = "3070"
    URL = f"http://localhost:{PORT}/login"
    
    driver = webdriver.Chrome()
    driver.maximize_window()
    
>>>>>>> 61c3cc00a000f2204436b07de06d74944b8999ba
    wait = WebDriverWait(driver, 10)

    try:
        driver.get(URL)

        # ✅ Wait for login form
        wait.until(EC.presence_of_element_located((By.NAME, "email")))

        # ✅ Enter credentials
        driver.find_element(By.NAME, "email").send_keys("admin@gmail.com")  
        driver.find_element(By.NAME, "password").send_keys("Test@123")

        # ✅ Click login
        login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
        driver.execute_script("arguments[0].scrollIntoView(true);", login_btn)
        driver.execute_script("arguments[0].click();", login_btn)

        # ✅ Wait for page load
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        current_url = driver.current_url.lower()
        page_text = driver.find_element(By.TAG_NAME, "body").text.lower()

        print("👉 Current URL:", current_url)

        # ✅ SUCCESS CONDITIONS
        if "/citizen" in current_url:
            print("✅ Login SUCCESS → /citizen")

        elif "dashboard" in current_url:
            print("✅ Login SUCCESS → dashboard")

        elif "welcome" in page_text or "logout" in page_text:
            print("✅ Login SUCCESS (content detected)")

        # ❌ FAILURE
        elif "invalid" in page_text or "error" in page_text:
            print("❌ Login FAILED (invalid credentials)")

        else:
            print("⚠️ Login result unclear → check UI")

    except Exception as e:
        print("❌ Error:", e)

    finally:
        driver.quit()

<<<<<<< HEAD
if __name__ == "__main__":
    TEST_USER_LOGIN()
=======

if __name__ == "__main__":
    TEST_USER_LOGIN()
>>>>>>> 61c3cc00a000f2204436b07de06d74944b8999ba
