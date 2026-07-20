import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.settings import Config 

class ProductPage(BasePage):
    
    #LOCATORS:
    PHONE_CATEGORY_LINK = (By.LINK_TEXT, "Phones")
    PHONE_LINK = (By.LINK_TEXT, "Iphone 6 32gb")
    PHONE_NAME = (By.CSS_SELECTOR, ".name")
    PHONE_PRICE_LABEL = (By.CSS_SELECTOR, ".price-container")
    PHONE_DESC_TEXT = (By.CSS_SELECTOR, "#more-information > p")
    
    LAPTOP_CATEGORY_LINK = (By.LINK_TEXT, "Laptops")
    LAPTOP_LINK = (By.LINK_TEXT, "MacBook Pro")
    LAPTOP_NAME = (By.CSS_SELECTOR, ".name")
    LAPTOP_PRICE_LABEL = (By.CSS_SELECTOR, ".price-container")
    LAPTOP_DESC_TEXT = (By.CSS_SELECTOR, "#more-information > p")
    
    @allure.step("Navigate to the website")
    def open(self):
        self.open_url(Config.BASE_URL)
    
    @allure.step("Click 'Phones' category")
    def click_phone_category(self):
        self.click(*self.PHONE_CATEGORY_LINK)
    
    @allure.step("Select phone product")
    def click_phone(self):
        self.click(*self.PHONE_LINK)
    
    @allure.step("Verify phone name")    
    def get_phone_name(self):
        return self.get_text(*self.PHONE_NAME)
    
    @allure.step("Verify phone price")   
    def get_phone_price(self):
        return self.get_text(*self.PHONE_PRICE_LABEL)
    
    @allure.step("Verify phone description")   
    def get_phone_description(self):
        return self.get_text(*self.PHONE_DESC_TEXT)
    
    @allure.step("Click 'Laptops' category")
    def click_laptop_category(self):
        self.click(*self.LAPTOP_CATEGORY_LINK)
    
    @allure.step("Select laptop product")
    def click_laptop(self):
        self.click(*self.LAPTOP_LINK)
        
    @allure.step("Verify laptop name")    
    def get_laptop_name(self):
        return self.get_text(*self.LAPTOP_NAME)
    
    @allure.step("Verify laptop price")   
    def get_laptop_price(self):
        return self.get_text(*self.LAPTOP_PRICE_LABEL)
    
    @allure.step("Verify laptop description")   
    def get_laptop_description(self):
        return self.get_text(*self.LAPTOP_DESC_TEXT)