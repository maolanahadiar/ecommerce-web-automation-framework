import pytest
from pages.product_page import ProductPage
from testdata.products import PRODUCTS_DATA

@pytest.fixture
def open_product(logged_in_user):
    product_page = ProductPage(logged_in_user)
    phone = PRODUCTS_DATA["phone"]
    
    product_page.click_phone_category()
    product_page.click_phone()
    
    assert product_page.get_phone_name() == phone["name"]
    
    return logged_in_user