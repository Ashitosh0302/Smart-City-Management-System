from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ---------------- CONFIG ----------------
PORT = "3070"
BASE_URL = f"http://localhost:{PORT}"
APPOINTMENT_URL = f"{BASE_URL}/citizen/appointments/hospital"

# ---------------- SETUP DRIVER ----------------
driver = webdriver.Chrome()   # or webdriver.Firefox()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

try:
    # 1. Open page
    driver.get(APPOINTMENT_URL)

    # 2. Select hospital (City Hospital card)
    city_hospital = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".hospital-card[data-hospital='city']"))
    )
    city_hospital.click()

    # 3. Fill Patient Name
    driver.find_element(By.ID, "patientName").send_keys("Anushka Wagh")

    # 4. Fill Age
    driver.find_element(By.ID, "age").send_keys("21")

    # 5. Select Gender
    driver.find_element(By.ID, "female").click()

    # 6. Contact Number
    driver.find_element(By.ID, "contactNumber").send_keys("9876543210")

    # 7. Address
    driver.find_element(By.ID, "address").send_keys("Jamnagar, Gujarat")

    # 8. Purpose
    driver.find_element(By.ID, "purpose").send_keys("General Checkup")

    # 9. Appointment Date (already auto-set, but can change)
    date_input = driver.find_element(By.ID, "appointmentDate")
    driver.execute_script("arguments[0].value = arguments[1]", date_input, "2026-04-20")

    # 10. Select Time Slot (choose first available)
    time_slot = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".time-slot"))
    )
    time_slot.click()

    # 11. Submit form
    submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_btn.click()

    # 12. Wait for success message
    success = wait.until(
        EC.presence_of_element_located((By.ID, "successMessage"))
    )

    # 13. Assertion / Verification
    assert "Appointment Booked Successfully" in success.text

    print("✅ TEST PASSED: Appointment booked successfully!")

    time.sleep(3)

except Exception as e:
    print("❌ TEST FAILED:", e)

finally:
    driver.quit()
