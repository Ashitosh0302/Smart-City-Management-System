import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "http://localhost:3070/government"  # change if needed


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def wait(driver, time=10):
    return WebDriverWait(driver, time)


# -------------------- 1. PAGE LOAD TEST --------------------
def test_page_load(driver):
    driver.get(BASE_URL)
    assert "CityZen" in driver.title


# -------------------- 2. HEADER TEST --------------------
def test_header_elements(driver):
    driver.get(BASE_URL)

    logo = wait(driver).until(
        EC.presence_of_element_located((By.CLASS_NAME, "govt-logo"))
    )
    assert logo is not None

    title = driver.find_element(By.TAG_NAME, "h1")
    assert "CityZen" in title.text


# -------------------- 3. STATS DISPLAY TEST --------------------
def test_stats_cards(driver):
    driver.get(BASE_URL)

    wait(driver).until(
        EC.presence_of_element_located((By.CLASS_NAME, "stat-card"))
    )

    stats = driver.find_elements(By.CLASS_NAME, "stat-card")
    assert len(stats) >= 3


# -------------------- 4. CATEGORY CARDS TEST --------------------
def test_category_cards(driver):
    driver.get(BASE_URL)

    cards = wait(driver).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "category-card"))
    )

    assert len(cards) == 4  # water, garbage, electricity, road


# -------------------- 5. CATEGORY NAVIGATION TEST --------------------
def test_category_navigation(driver):
    driver.get(BASE_URL)

    # Click Water Complaint card
    water_card = driver.find_element(By.CSS_SELECTOR, ".water-card")
    water_card.click()

    # Check navigation
    assert "water" in driver.current_url


# -------------------- 6. GARBAGE CARD NAVIGATION --------------------
def test_garbage_navigation(driver):
    driver.get(BASE_URL)

    garbage_card = driver.find_element(By.CSS_SELECTOR, ".garbage-card")
    garbage_card.click()

    assert "garbage" in driver.current_url


# -------------------- 7. ELECTRICITY NAVIGATION --------------------
def test_electricity_navigation(driver):
    driver.get(BASE_URL)

    elec_card = driver.find_element(By.CSS_SELECTOR, ".electricity-card")
    elec_card.click()

    assert "electricity" in driver.current_url


# -------------------- 8. ROAD NAVIGATION --------------------
def test_road_navigation(driver):
    driver.get(BASE_URL)

    road_card = driver.find_element(By.CSS_SELECTOR, ".traffic-card")
    road_card.click()

    assert "road" in driver.current_url


# -------------------- 9. LOGOUT BUTTON TEST --------------------
def test_logout_button(driver):
    driver.get(BASE_URL)

    logout = wait(driver).until(
        EC.presence_of_element_located((By.CLASS_NAME, "logout-btn-header"))
    )

    assert logout.is_displayed()


# -------------------- 10. STAT VALUE NOT EMPTY TEST --------------------
def test_stat_values(driver):
    driver.get(BASE_URL)

    values = driver.find_elements(By.CLASS_NAME, "stat-value")

    for v in values:
        assert v.text is not None


# -------------------- 11. RESPONSIVE CHECK (basic) --------------------
def test_mobile_view(driver):
    driver.set_window_size(375, 812)  # iPhone size
    driver.get(BASE_URL)

    cards = driver.find_elements(By.CLASS_NAME, "category-card")
    assert len(cards) > 0
