import pytest
import allure
from pages.product_page import ProductPage
from testdata.products import PRODUCTS_DATA

@allure.title("Verify phone details are displayed correctly")
@pytest.mark.skip_ci
def test_phone_detail(browser):
    product_page = ProductPage(browser)
    phone = PRODUCTS_DATA["phone"]
    
    product_page.open()
    product_page.click_phone_category()
    product_page.click_phone()

    assert product_page.get_phone_name() == phone["name"]
    assert phone["price"] in product_page.get_phone_price()
    assert phone["description"] in product_page.get_phone_description()
    
@allure.title("Verify laptop details are displayed correctly")
def test_laptop_detail(browser):
    product_page = ProductPage(browser)
    laptop = PRODUCTS_DATA["laptop"]

    product_page.open()
    product_page.click_laptop_category()
    product_page.click_laptop()
    
    assert product_page.get_laptop_name() == laptop["name"]
    assert laptop["price"] in product_page.get_laptop_price()
    assert laptop["description"] in product_page.get_laptop_description()