import pytest
from pages.cart_page import CartPage

@pytest.fixture
def add_product_to_cart(open_product):
    cart_page = CartPage(open_product)
    
    cart_page.add_phone_to_cart()
    
    return open_product