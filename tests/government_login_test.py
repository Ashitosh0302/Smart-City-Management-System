from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def LOGIN_TEST(user_input, password):
    PORT = "3070"
    URL = "http://localhost:3070/login"

    edge_options = Options()
    edge_options.add_argument("--headless")
    edge_options.add_argument("--no-sandbox")
    edge_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=edge_options)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get(URL)

        # ===============================
        # ✅ STEP 1: Click Authority
        # ===============================
        admin_box = wait.until(EC.presence_of_element_located((By.ID, "adminBox")))

        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", admin_box)
        wait.until(EC.element_to_be_clickable((By.ID, "adminBox")))

        driver.execute_script("arguments[0].click();", admin_box)

        # ===============================
        # ✅ STEP 2: Wait for Department dropdown
        # ===============================
        dept_dropdown = wait.until(EC.visibility_of_element_located((By.NAME, "department")))

        # ===============================
        # ✅ STEP 3: Select Government
        # ===============================
        select = Select(dept_dropdown)
        select.select_by_value("government")

        # ===============================
        # ✅ STEP 4: Enter Email
        # ===============================
        email_input = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
        email_input.clear()
        email_input.send_keys(user_input)

        # ===============================
        # ✅ STEP 5: Enter Password
        # ===============================
        password_input = driver.find_element(By.NAME, "password")
        password_input.clear()
        password_input.send_keys(password)

        # ===============================
        # ✅ STEP 6: Click Login
        # ===============================
        login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))

        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", login_btn)
        driver.execute_script("arguments[0].click();", login_btn)

        # ===============================
        # ✅ STEP 7: Verify Login
        # ===============================
        wait.until(lambda d: d.current_url != URL)

        if "dashboard" in driver.current_url.lower():
            print(f"✅ Login successful with: {user_input}")
        else:
            print(f"❌ Login failed with: {user_input}")

    except Exception as e:
        print("❌ Error:", e)

    finally:
        driver.quit()

# ===============================
# ✅ RUN TEST
# ===============================

if __name__ == "__main__":
    LOGIN_TEST("gov8517@gmail.com","Gov@123")
