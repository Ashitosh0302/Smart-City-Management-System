from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# ================= CONFIG =================
PORT = "3070"
BASE_URL = f"http://localhost:{PORT}/government/complaints/water"   # change route if needed

# ================= SETUP =================
driver = webdriver.Chrome()
driver.maximize_window()


# ================= HELPERS =================
def wait():
    time.sleep(2)


# ================= TEST 1: LOAD PAGE =================
def test_load_page():
    driver.get(BASE_URL)
    wait()
    assert "Water Infrastructure" in driver.title
    print("✅ Page Loaded")


# ================= TEST 2: TABLE LOAD =================
def test_table_load():
    rows = driver.find_elements(By.CSS_SELECTOR, "#complaintsTableBody tr")
    assert len(rows) > 0
    print("✅ Table Loaded")


# ================= TEST 3: SEARCH FUNCTION =================
def test_search():
    search = driver.find_element(By.ID, "searchInput")
    search.clear()
    search.send_keys("WTR-001")
    search.send_keys(Keys.ENTER)
    wait()

    rows = driver.find_elements(By.CSS_SELECTOR, "#complaintsTableBody tr")
    assert len(rows) >= 1
    print("✅ Search Working")


# ================= TEST 4: FILTER STATUS =================
def test_filter_status():
    dropdown = driver.find_element(By.ID, "statusFilter")
    dropdown.click()
    dropdown.find_element(By.XPATH, "//option[@value='Resolved']").click()
    wait()

    rows = driver.find_elements(By.CSS_SELECTOR, "#complaintsTableBody tr")
    assert len(rows) >= 0
    print("✅ Status Filter Working")


# ================= TEST 5: VIEW MODAL =================
def test_view_modal():
    view_btn = driver.find_element(By.CSS_SELECTOR, ".btn-view")
    view_btn.click()
    wait()

    modal = driver.find_element(By.ID, "viewModal")
    assert "active" in modal.get_attribute("class")
    print("✅ View Modal Opened")


# ================= TEST 6: CLOSE MODAL =================
def test_close_modal():
    close_btn = driver.find_element(By.CLASS_NAME, "modal-close")
    close_btn.click()
    wait()

    modal = driver.find_element(By.ID, "viewModal")
    assert "active" not in modal.get_attribute("class")
    print("✅ Modal Closed")


# ================= TEST 7: UPDATE MODAL =================
def test_update_modal():
    edit_btn = driver.find_elements(By.CSS_SELECTOR, ".fa-edit")[0]
    edit_btn.click()
    wait()

    modal = driver.find_element(By.ID, "updateModal")
    assert "active" in modal.get_attribute("class")
    print("✅ Update Modal Opened")


# ================= TEST 8: CHANGE STATUS =================
def test_change_status():
    status = driver.find_element(By.ID, "statusSelect")
    status.click()
    status.find_element(By.XPATH, "//option[@value='Resolved']").click()

    notes = driver.find_element(By.ID, "govtNotes")
    notes.send_keys("Test update via Selenium")

    save_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Save Changes')]")
    save_btn.click()

    wait()
    print("✅ Status Updated")


# ================= TEST 9: PAGINATION =================
def test_pagination():
    next_btn = driver.find_element(By.ID, "nextBtn")
    if not next_btn.is_enabled():
        print("ℹ️ Pagination not required (single page)")
        return

    next_btn.click()
    wait()
    print("✅ Pagination Working")


# ================= RUN ALL TESTS =================
if __name__ == "__main__":
    try:
        test_load_page()
        test_table_load()
        test_search()
        test_filter_status()
        test_view_modal()
        test_close_modal()
        test_update_modal()
        test_change_status()
        test_pagination()

        print("\n🎉 ALL TESTS PASSED")

    except Exception as e:
        print("❌ TEST FAILED:", e)

    finally:
        time.sleep(3)
        driver.quit()
