from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.settings import Config
import allure

class LoginPage(BasePage):

    # LOCATORS
    LOGIN_MENU_BUTTON = (By.ID, "login2")
    LOGIN_MODAL_TITLE = (By.ID, "logInModalLabel")    
    USERNAME_INPUT = (By.ID, "loginusername")
    PASSWORD_INPUT = (By.ID, "loginpassword")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[onclick='logIn()']")
    LOGIN_SUCCESS_MESSAGE = (By.ID, "nameofuser")

    @allure.step("Navigate to the website")
    def open(self):
        self.open_url(Config.BASE_URL)
    
    @allure.step("Click login menu")
    def click_login_menu_button(self):
        self.click(*self.LOGIN_MENU_BUTTON)
        return self.get_text(*self.LOGIN_MODAL_TITLE)

    @allure.step("Input login form")
    def input_login_form(self, username, password):
        self.type(*self.USERNAME_INPUT, text=username)
        self.type(*self.PASSWORD_INPUT, text=password)
    
    @allure.step("Click login button")
    def click_login_button(self):
        self.click(*self.LOGIN_BUTTON)

    @allure.step("Verify login is successfully")
    def get_login_success_message(self):    
        return self.get_text(*self.LOGIN_SUCCESS_MESSAGE)
    
    @allure.step("Verify login is failed")
    def get_login_alert_message(self):
        alert = self.wait_alert()
        return alert.text

    @allure.step("Close alert popup")
    def accept_alert(self):
        alert = self.wait_alert()
        alert.accept()