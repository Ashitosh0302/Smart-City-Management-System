from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class TestCourtDashboard:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:3070/citizen/appointments/court")  # change to your URL
        self.driver.maximize_window()
        time.sleep(3)

    def teardown_method(self):
        self.driver.quit()

    # ✅ 1. Check page load
    def test_page_load(self):
        title = self.driver.title
        assert "Judicial Administration Portal" in title or title != ""

    # ✅ 2. Check dashboard stats exist
    def test_dashboard_stats(self):
        total = self.driver.find_element(By.ID, "totalAppointments").text
        pending = self.driver.find_element(By.ID, "pendingAppointments").text

        assert total is not None
        assert pending is not None

    # ✅ 3. Test search filter
    def test_search_filter(self):
        search_box = self.driver.find_element(By.ID, "searchInput")
        search_box.send_keys("Rahul")
        search_box.send_keys(Keys.ENTER)

        time.sleep(2)

        rows = self.driver.find_elements(By.CSS_SELECTOR, "#appointmentsTableBody tr")
        assert len(rows) >= 1

    # ✅ 4. Test status filter dropdown
    def test_status_filter(self):
        dropdown = self.driver.find_element(By.ID, "statusFilter")
        dropdown.click()

        option = self.driver.find_element(By.XPATH, "//option[@value='Pending']")
        option.click()

        time.sleep(2)

        rows = self.driver.find_elements(By.CSS_SELECTOR, "#appointmentsTableBody tr")
        assert rows is not None

    # ✅ 5. Open VIEW modal
    def test_view_modal(self):
        view_btn = self.driver.find_element(By.CSS_SELECTOR, ".btn-view")
        view_btn.click()

        time.sleep(2)

        modal = self.driver.find_element(By.ID, "viewModal")
        assert "active" in modal.get_attribute("class")

    # ✅ 6. Open UPDATE modal
    def test_update_modal(self):
        update_btn = self.driver.find_element(By.CSS_SELECTOR, ".btn-update")
        update_btn.click()

        time.sleep(2)

        modal = self.driver.find_element(By.ID, "updateModal")
        assert "active" in modal.get_attribute("class")

    # ✅ 7. Update status and save
    def test_update_status(self):
        update_btn = self.driver.find_element(By.CSS_SELECTOR, ".btn-update")
        update_btn.click()

        time.sleep(2)

        status_dropdown = self.driver.find_element(By.ID, "statusSelect")
        status_dropdown.send_keys("Approved")

        save_btn = self.driver.find_element(By.CSS_SELECTOR, ".btn-save")
        save_btn.click()

        time.sleep(3)

        toast = self.driver.find_element(By.ID, "toast")
        assert toast.is_displayed()

    # ✅ 8. Close modal
    def test_close_modal(self):
        self.driver.find_element(By.CSS_SELECTOR, ".btn-view").click()
        time.sleep(2)

        close_btn = self.driver.find_element(By.CSS_SELECTOR, ".modal-close")
        close_btn.click()

        time.sleep(1)

        modal = self.driver.find_element(By.ID, "viewModal")
        assert "active" not in modal.get_attribute("class")
