from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class LogoutPage(BasePage):

    #LOCATORS
    LOGOUT_BUTTON = (By.ID, "logout2")
    LOGIN_MENU_BUTTON = (By.ID, "login2")
    SIGNUP_MENU_BUTTON = (By.ID, "signin2")
    
    @allure.step("Click logout button")
    def click_logout_menu_button(self):
        self.click(*self.LOGOUT_BUTTON)
        
    @allure.step("Verify logout is successfully")
    def is_logged_out(self):
        return (
            self.element_visible(*self.LOGIN_MENU_BUTTON)
            and
            self.element_visible(*self.SIGNUP_MENU_BUTTON)
        )