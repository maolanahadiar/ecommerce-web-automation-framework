import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class CartPage(BasePage):
    
    #LOCATORS:  
    ADDING_CART_BUTTON = (By.LINK_TEXT, "Add to cart")
    CART_MENU = (By.ID, "cartur")
    CART_PHONE_NAME= (By.XPATH, "//td[contains(normalize-space(),'Iphone 6 32gb')]")
    CART_PHONE_PRICE_LABEL = (By.XPATH, "//td[contains(normalize-space(),'790')]")
    CART_DELETE_LINK = (By.LINK_TEXT, "Delete")
    
    @allure.step("Adding product to cart")   
    def add_phone_to_cart(self):
        self.click(*self.ADDING_CART_BUTTON)
        self.get_alert_and_accept()
        self.click(*self.CART_MENU)
    
    @allure.step("Verify product name in cart") 
    def get_phone_name_in_cart(self):
        return self.get_text(*self.CART_PHONE_NAME)
    
    @allure.step("Verify product price in cart")
    def get_phone_price_in_cart(self):
        return self.get_text(*self.CART_PHONE_PRICE_LABEL)
    
    @allure.step("Delete product in cart")
    def delete_products_in_cart(self):
        self.click(*self.CART_DELETE_LINK)
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element(self.CART_DELETE_LINK)
            )
        
    @allure.step("Verify product is deleted") 
    def is_product_displayed(self):
        return (
            self.is_element_displayed(*self.CART_PHONE_NAME)
            and
            self.is_element_displayed(*self.CART_PHONE_PRICE_LABEL)
            )