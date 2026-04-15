from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ---------------- CONFIG ----------------
PORT = "3070"
BASE_URL = f"http://localhost:{PORT}"
E_KYC_URL = f"{BASE_URL}/citizen/appointments/esetu"

# ---------------- SETUP ----------------

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    edge_options = Options()
    edge_options.add_argument("--headless")
    edge_options.add_argument("--no-sandbox")
    edge_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=edge_options)
    ), options=chrome_options)
    
driver.maximize_window()
wait = WebDriverWait(driver, 10)

try:
    # 1. Open page
    driver.get(E_KYC_URL)

    # 2. Fill Citizen Details
    driver.find_element(By.ID, "fullName").send_keys("Anushka Wagh")
    driver.find_element(By.ID, "mobileNumber").send_keys("9876543210")
    driver.find_element(By.ID, "email").send_keys("anushka@example.com")

    # 3. Select Service Type (Income Certificate)
    driver.find_element(By.ID, "incomeCert").click()

    # 4. Select Center Location (City Center)
    driver.find_element(By.ID, "cityCenter").click()

    # 5. Set Appointment Date (tomorrow or fixed date)
    date_input = driver.find_element(By.ID, "appointmentDate")
    driver.execute_script("arguments[0].value = arguments[1]", date_input, "2026-04-20")

    # 6. Select Time Slot (10-11 AM)
    driver.find_element(By.ID, "slot1").click()

    # 7. Add Remarks
    driver.find_element(By.ID, "remarks").send_keys("Need Aadhaar update assistance")

    # 8. Submit form
    submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_btn.click()

    # 9. Wait for page response (if success message exists OR redirect)
    time.sleep(3)

    print("✅ TEST COMPLETED: Form submitted successfully!")

except Exception as e:
    print("❌ TEST FAILED:", e)

finally:
    driver.quit()
