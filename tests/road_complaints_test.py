from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# =========================
# CONFIGURATION
# =========================
PORT = "3070"
BASE_URL = f"http://localhost:{PORT}/login"
ROAD_URL = f"{BASE_URL}/citizen/complaints/roads"

# =========================
# SETUP DRIVER
# =========================

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

try:
    # =========================
    # OPEN PAGE
    # =========================
    driver.get(ROAD_URL)
    time.sleep(2)

    # =========================
    # LOCATION DETAILS
    # =========================
    driver.find_element(By.ID, "roadName").send_keys("MG Road")
    driver.find_element(By.ID, "area").send_keys("Andheri West")
    driver.find_element(By.ID, "ward").send_keys("Ward 1")
    driver.find_element(By.ID, "city").clear()
    driver.find_element(By.ID, "city").send_keys("Mumbai")
    driver.find_element(By.ID, "pincode").send_keys("400001")

    # Landmark (optional)
    landmark = driver.find_element(By.NAME, "landmark")
    landmark.send_keys("Near Metro Station")

    time.sleep(1)

    # =========================
    # ISSUE TYPE (click potholes or others)
    # =========================
    driver.find_element(By.ID, "issueType").click  # hidden input (JS controlled)

    # Click UI card instead
    driver.find_element(By.XPATH, "//div[contains(text(),'Potholes')]").click()

    # =========================
    # SECURITY LEVEL
    # =========================
    driver.find_element(By.XPATH, "//div[contains(text(),'Dangerous')]").click()

    # =========================
    # AFFECTED AREA
    # =========================
    driver.find_element(By.XPATH, "//div[contains(text(),'Large Area')]").click()

    # =========================
    # DURATION
    # =========================
    driver.find_element(By.NAME, "durationValue").clear()
    driver.find_element(By.NAME, "durationValue").send_keys("3")

    driver.find_element(By.NAME, "durationUnit").send_keys("days")

    # =========================
    # WEATHER ISSUE
    # =========================
    driver.find_element(By.NAME, "monsoonIssue").send_keys("Rainwater Accumulation")

    # =========================
    # REMARKS
    # =========================
    driver.find_element(By.NAME, "remarks").send_keys(
        "Large potholes causing traffic issue and accidents risk."
    )

    # =========================
    # DATE & TIME
    # =========================
    driver.find_element(By.NAME, "captureDate").send_keys("13042026")
    driver.find_element(By.NAME, "captureTime").send_keys("1030AM")

    time.sleep(1)

    # =========================
    # SUBMIT FORM
    # =========================
    submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_btn.click()

    print("✅ Road complaint submitted successfully!")

    # Wait for modal / response
    time.sleep(5)

except Exception as e:
    print("❌ Test Failed:", e)

finally:
    driver.quit()
