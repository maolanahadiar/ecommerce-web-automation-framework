from pages.product_page import ProductPage
from data.product_data import PRODUCTS
import allure
import pytest

@allure.title("Verify phone details are displayed correctly")
@pytest.mark.skip_ci
def test_phone_detail(browser):
    product_page = ProductPage(browser)
    phone = PRODUCTS["phone"]
    
    product_page.open()
    product_page.click_phone_category()
    product_page.click_phone()

    assert phone["name"] == product_page.get_phone_name()
    assert phone["price"] in product_page.get_phone_price()
    assert phone["description"] in product_page.get_phone_description()
    
@allure.title("Verify laptop details are displayed correctly")
def test_laptop_detail(browser):
    product_page = ProductPage(browser)
    laptop = PRODUCTS["laptop"]
    
    product_page.open()
    product_page.click_laptop_category()
    product_page.click_laptop()
    
    assert laptop["name"] == product_page.get_laptop_name()
    assert laptop["price"] in product_page.get_laptop_price()
    assert laptop["description"] in product_page.get_laptop_description()