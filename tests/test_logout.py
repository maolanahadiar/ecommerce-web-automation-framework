import pytest
import allure
from pages.logout_page import LogoutPage

@pytest.mark.smoke
@pytest.mark.regression
@allure.title("Verify user can logout successfully")
def test_logout_success(logged_in_user):
    logout_page = LogoutPage(logged_in_user)

    logout_page.click_logout_menu_button()
    
    assert logout_page.is_logged_out()