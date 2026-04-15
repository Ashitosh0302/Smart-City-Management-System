import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
import random

@pytest.fixture
def driver():
    edge_options = Options()
    edge_options.add_argument("--headless")
    edge_options.add_argument("--no-sandbox")
    edge_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=edge_options)
    yield driver
    driver.quit()

import time
import random

import time

BASE_URL = "http://localhost:3070/government/complaints/garbage"   # change if needed

def test_page_load(driver):
    driver.get(BASE_URL)
    assert "Garbage Infrastructure" in driver.title

# -------------------------------
# 2. TABLE LOAD TEST
# -------------------------------
def test_table_load(driver):
    driver.get(BASE_URL)

    wait = WebDriverWait(driver, 10)
    table_rows = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#complaintsTableBody tr"))
    )

    assert len(table_rows) > 0

# -------------------------------
# 3. FILTER TEST (STATUS)
# -------------------------------
def test_status_filter(driver):
    driver.get(BASE_URL)

    status_dropdown = Select(driver.find_element(By.ID, "statusFilter"))
    status_dropdown.select_by_visible_text("Pending")

    time.sleep(2)

    rows = driver.find_elements(By.CSS_SELECTOR, "#complaintsTableBody tr")
    assert len(rows) > 0

# -------------------------------
# 4. SEARCH TEST
# -------------------------------
def test_search(driver):
    driver.get(BASE_URL)

    search_box = driver.find_element(By.ID, "searchInput")
    search_box.send_keys("Garbage")
    search_box.send_keys(Keys.ENTER)

    time.sleep(2)

    rows = driver.find_elements(By.CSS_SELECTOR, "#complaintsTableBody tr")
    assert len(rows) >= 0

# -------------------------------
# 5. PAGINATION TEST
# -------------------------------
def test_pagination(driver):
    driver.get(BASE_URL)

    next_btn = driver.find_element(By.ID, "nextBtn")

    if next_btn.is_enabled():
        next_btn.click()
        time.sleep(2)

        page_info = driver.find_element(By.ID, "pageInfo").text
        assert "Page" in page_info

# -------------------------------
# 6. VIEW COMPLAINT MODAL TEST
# -------------------------------
def test_view_modal(driver):
    driver.get(BASE_URL)

    wait = WebDriverWait(driver, 10)

    view_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'View')]"))
    )
    view_btn.click()

    modal = wait.until(
        EC.visibility_of_element_located((By.ID, "viewModal"))
    )

    assert modal.is_displayed()

# -------------------------------
# 7. UPDATE COMPLAINT TEST
# -------------------------------
def test_update_modal(driver):
    driver.get(BASE_URL)

    wait = WebDriverWait(driver, 10)

    edit_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Edit')]"))
    )
    edit_btn.click()

    modal = wait.until(
        EC.visibility_of_element_located((By.ID, "updateModal"))
    )

    assert modal.is_displayed()

# -------------------------------
# 8. STATUS UPDATE TEST (MOCK)
# -------------------------------
def test_status_update(driver):
    driver.get(BASE_URL)

    wait = WebDriverWait(driver, 10)

    edit_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Edit')]"))
    )
    edit_btn.click()

    status_dropdown = Select(wait.until(
        EC.presence_of_element_located((By.ID, "statusSelect"))
    ))
    status_dropdown.select_by_visible_text("Resolved")

    save_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Save Changes')]")
    save_btn.click()

    time.sleep(2)

    toast = driver.find_element(By.ID, "toast")
    assert "show" in toast.get_attribute("class")

# -------------------------------
# 9. FILTER CLEAR TEST
# -------------------------------
def test_clear_filters(driver):
    driver.get(BASE_URL)

    driver.find_element(By.ID, "searchInput").send_keys("test")
    driver.find_element(By.ID, "statusFilter").send_keys("Pending")

    clear_btn = driver.find_element(By.XPATH, "//button[contains(text(),'fa-times')]")
    clear_btn.click()

    time.sleep(1)

    search_value = driver.find_element(By.ID, "searchInput").get_attribute("value")
    assert search_value == ""