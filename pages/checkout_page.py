from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class CheckoutPage(BasePage):
    
    #LOCATORS:  
    ORDER_BUTTON = (By.CSS_SELECTOR, ".btn.btn-success")
    NAME_INPUT = (By.ID, "name")
    COUNTRY_INPUT = (By.ID, "country")
    CITY_INPUT = (By.ID, "city")
    CARD_INPUT = (By.ID, "card")
    MONTH_INPUT = (By.ID, "month")
    YEAR_INPUT = (By.ID, "year")
    PURCHASE_BUTTON = (By.XPATH, "//button[normalize-space()='Purchase']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.sweet-alert > h2")
    OK_BUTTON = (By.CSS_SELECTOR, "div.sa-button-container > div.sa-confirm-button-container > button.confirm")
    
    @allure.step("Place order")
    def place_order(self):
        self.click(*self.ORDER_BUTTON)

    @allure.step("Input billing detail")
    def input_billing_details(self, name, country, city, card_number, month, year):
        self.type(*self.NAME_INPUT,text=name)
        self.type(*self.COUNTRY_INPUT,text=country)
        self.type(*self.CITY_INPUT,text=city)
        self.type(*self.CARD_INPUT,text=card_number)
        self.type(*self.MONTH_INPUT,text=month)
        self.type(*self.YEAR_INPUT,text=year)
        
    @allure.step("Checkout order")
    def checkout_order(self):
        self.click(*self.PURCHASE_BUTTON)
        
    @allure.step("Verify checkout is successfully")
    def get_checkout_success_message(self):    
        return self.get_text(*self.SUCCESS_MESSAGE)
    
    @allure.step("Close success popup")
    def close_success_popup(self):
        self.click(*self.OK_BUTTON)