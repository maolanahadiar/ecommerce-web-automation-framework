import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config.settings import Config
from utils.allure_helper import AllureHelper as allure

RESULTS_DIR = "reports/allure-results"
REPORT_DIR = "reports/allure-report"

#setup browser fixture for tests
@pytest.fixture
def browser():
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
    
pytest_plugins = [
    "fixtures.login_fixture",
    "fixtures.product_fixture",
    "fixtures.cart_fixture"
]

def pytest_sessionstart(session):
    allure.create_environment(RESULTS_DIR)
    allure.create_executor(RESULTS_DIR)
    allure.create_categories(RESULTS_DIR)

def pytest_sessionfinish(session, exitstatus):
    allure.copy_history(
        RESULTS_DIR,
        REPORT_DIR
    )
    
    allure.generate_report(
        RESULTS_DIR,
        REPORT_DIR
    )
    if Config.AUTO_OPEN_REPORT == True:
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