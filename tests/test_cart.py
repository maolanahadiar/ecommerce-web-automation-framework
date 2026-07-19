from pages.cart_page import CartPage
from data.product_data import PRODUCTS
import allure
import pytest

@allure.title("Verify user can add product to cart")
@pytest.mark.skip_ci
def test_product_detail_in_cart(open_product):
    cart_page = CartPage(open_product)
    phone = PRODUCTS["phone"]
    
    cart_page.add_phone_to_cart()
    
    assert phone["name"] in cart_page.get_phone_name_in_cart()
    assert phone["price"] in cart_page.get_phone_price_in_cart()
    
    cart_page.delete_products_in_cart()

@allure.title("Verify user can remove product from cart")
def test_delete_product_in_cart(open_product):
    cart_page = CartPage(open_product)
    
    cart_page.add_phone_to_cart()
    cart_page.delete_products_in_cart()
    
    assert not cart_page.is_product_displayed()