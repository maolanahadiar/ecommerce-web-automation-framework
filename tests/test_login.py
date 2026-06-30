import pytest
import allure
from pages.login_page import LoginPage
from data.login_data import VALID_CREDENTIALS, INVALID_CREDENTIALS

@allure.title("Verify user can login with valid credentials")
def test_login_success(browser):  
    login_page = LoginPage(browser)

    login_page.open()
    login_page.click_login_menu_button()
    login_page.input_login_form(
        VALID_CREDENTIALS["username"],
        VALID_CREDENTIALS["password"]
    )
    login_page.click_login_button()

    assert VALID_CREDENTIALS["expected"] == login_page.get_login_success_message()

@pytest.mark.parametrize("INVALID_CREDENTIALS",INVALID_CREDENTIALS)
def test_login_failed(browser, INVALID_CREDENTIALS):
    
    allure.dynamic.title(
        f"Verify user cannot login with invalid credentials - {INVALID_CREDENTIALS['case']}"
    )
    login_page = LoginPage(browser)

    login_page.open()
    login_page.click_login_menu_button()
    login_page.input_login_form(
        INVALID_CREDENTIALS["username"],
        INVALID_CREDENTIALS["password"]
    )
    login_page.click_login_button()

    assert INVALID_CREDENTIALS["expected"] == login_page.get_login_alert_message()
    login_page.accept_alert()