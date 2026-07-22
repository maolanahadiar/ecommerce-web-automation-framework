import pytest
import allure
from pages.cart_page import CartPage
from testdata.products import PRODUCTS_DATA

@pytest.mark.skip_ci
@pytest.mark.regression
@allure.title("Verify user can add product to cart")
def test_product_detail_in_cart(open_product):
    cart_page = CartPage(open_product)
    phone = PRODUCTS_DATA["phone"]
    
    cart_page.add_phone_to_cart()
    
    assert cart_page.get_phone_name_in_cart() == phone["name"]
    assert cart_page.get_phone_price_in_cart() == phone["price"]
    
    cart_page.delete_products_in_cart()

@pytest.mark.regression
@allure.title("Verify user can remove product from cart")
def test_delete_product_in_cart(open_product):
    cart_page = CartPage(open_product)
    
    cart_page.add_phone_to_cart()
    cart_page.delete_products_in_cart()
    
    assert not cart_page.is_product_displayed()