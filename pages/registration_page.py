import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.settings import Config

class RegistrationPage(BasePage):
    
    #LOCATORS
    SIGN_UP_MENU = (By.ID, "signin2")
    SIGN_UP_MODAL_TITLE = (By.ID, "signInModalLabel")
    USERNAME_INPUT = (By.ID, "sign-username")
    PASSWORD_INPUT = (By.ID, "sign-password")
    SIGN_UP_BUTTON = (By.XPATH, "//button[normalize-space()='Sign up']")
    
    @allure.step("Navigate to the website")
    def open(self):
        self.open_url(Config.BASE_URL)
        
    @allure.step("Click sign up menu")
    def click_registration_menu(self):
        self.click(*self.SIGN_UP_MENU)
        
    @allure.step("Verify registration popup modal")
    def get_registration_popup_screen(self):
        return self.get_text(*self.SIGN_UP_MODAL_TITLE)
    
    @allure.step("Input registration form")
    def input_registration_form(self, username, password):
        self.type(*self.USERNAME_INPUT, text=username)
        self.type(*self.PASSWORD_INPUT, text=password)
        
    @allure.step("Submit registration")
    def click_registration_button(self):
        self.click(*self.SIGN_UP_BUTTON)
        
    @allure.step("Verify registration is successfully")
    def get_registration_success_message(self):
        return self.get_alert_and_accept()
    
    @allure.step("Verify registration is failed")
    def get_registration_error_message(self):
        return self.get_alert_and_accept()