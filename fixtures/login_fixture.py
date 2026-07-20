import pytest
from pages.login_page import LoginPage
from testdata.credentials import VALID_CREDENTIALS

@pytest.fixture
def logged_in_user(browser):
    login_page = LoginPage(browser)
    
    login_page.open()
    login_page.click_login_menu()
    login_page.input_login_form(
        VALID_CREDENTIALS["username"],
        VALID_CREDENTIALS["password"]
    )
    login_page.click_login_button()

    assert login_page.get_login_success_message() == VALID_CREDENTIALS["expected_message"]
    
    return browser