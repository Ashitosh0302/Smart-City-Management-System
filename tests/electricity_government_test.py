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

BASE_URL = "http://localhost:3070/government/complaints/electricity"  # change as needed

def test_page_load(driver):
    assert "Electricity Infrastructure" in driver.title
    time.sleep(2)

    total = driver.find_element(By.ID, "totalComplaints")
    assert total is not None

# -------------------------
# 2. Table Load Test
# -------------------------
def test_table_load(driver):
    time.sleep(3)
    rows = driver.find_elements(By.CSS_SELECTOR, "#complaintsTableBody tr")
    assert len(rows) > 0

# -------------------------
# 3. Filter Test (Status)
# -------------------------
def test_status_filter(driver):
    time.sleep(2)

    status_dropdown = driver.find_element(By.ID, "statusFilter")
    status_dropdown.click()

    option = driver.find_element(By.XPATH, "//option[@value='Pending']")
    option.click()

    time.sleep(2)

    rows = driver.find_elements(By.CSS_SELECTOR, "#complaintsTableBody tr")
    assert len(rows) >= 0

# -------------------------
# 4. Search Test
# -------------------------
def test_search(driver):
    search = driver.find_element(By.ID, "searchInput")
    search.clear()
    search.send_keys("Rahul")
    search.send_keys(Keys.ENTER)

    time.sleep(2)

    rows = driver.find_elements(By.CSS_SELECTOR, "#complaintsTableBody tr")
    assert rows is not None

# -------------------------
# 5. View Modal Test
# -------------------------
def test_view_modal(driver):
    time.sleep(2)

    view_btn = driver.find_element(By.CSS_SELECTOR, ".action-btn-small")
    view_btn.click()

    time.sleep(2)

    modal = driver.find_element(By.ID, "viewModal")
    assert "active" in modal.get_attribute("class")

    close_btn = driver.find_element(By.CSS_SELECTOR, ".modal-close")
    close_btn.click()

# -------------------------
# 6. Update Modal Test
# -------------------------
def test_update_modal(driver):
    time.sleep(2)

    update_btns = driver.find_elements(By.CSS_SELECTOR, ".btn-update")
    update_btns[0].click()

    time.sleep(2)

    status_select = driver.find_element(By.ID, "statusSelect")
    status_select.send_keys("Resolved")

    save_btn = driver.find_element(By.CSS_SELECTOR, ".btn-save")
    save_btn.click()

    time.sleep(2)

# -------------------------
# 7. Pagination Test
# -------------------------
def test_pagination(driver):
    time.sleep(2)

    next_btn = driver.find_element(By.ID, "nextBtn")

    if next_btn.is_enabled():
        next_btn.click()
        time.sleep(2)

        page_info = driver.find_element(By.ID, "pageInfo")
        assert "Page" in page_info.text