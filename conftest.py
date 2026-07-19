import pytest
import shutil
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.allure_helper import AllureHelper as allure
from config.settings import Config

#setup browser fixture for tests
@pytest.fixture
def browser():
    options = Options()

    if Config.HEADLESS:
        options.add_argument("--headless=new")

    options.add_argument(f"--window-size={Config.WINDOW_SIZE}")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()

#configur custom fixtures    
pytest_plugins = [
    "fixtures.login_fixture",
    "fixtures.product_fixture",
    "fixtures.cart_fixture"
]

#allure report output directories
RESULTS_DIR = "reports/allure-results"
REPORT_DIR = "reports/allure-report"

#create allure metadata
def pytest_sessionstart(session):
    if os.path.exists(RESULTS_DIR):
        shutil.rmtree(RESULTS_DIR)

    os.makedirs(RESULTS_DIR, exist_ok=True)
    
    allure.create_environment(RESULTS_DIR)
    allure.create_executor(RESULTS_DIR)
    allure.create_categories(RESULTS_DIR)
    
#preserve report history and generate allure report based on config
def pytest_sessionfinish(session, exitstatus):
    allure.copy_history(
        RESULTS_DIR,
        REPORT_DIR
    )

    if Config.AUTO_OPEN_REPORT:
        allure.generate_report(
            RESULTS_DIR,
            REPORT_DIR
        )

        allure.open_report(REPORT_DIR)
        
#setup allure screenshot when test is failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call":
        return
    if report.failed:
        driver = item.funcargs.get("browser")
        if driver:
            allure.attach_screenshot(driver)