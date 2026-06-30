import pytest
from pages.product_page import ProductPage
from data.product_data import PRODUCTS

@pytest.fixture
def open_product(logged_in_user):
    product_page = ProductPage(logged_in_user)
    phone = PRODUCTS["phone"]
    
    product_page.click_phone_category()
    product_page.click_phone()
    
    assert phone["name"] == product_page.get_phone_name()
    
    return logged_in_user