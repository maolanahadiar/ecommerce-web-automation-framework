from pages.checkout_page import CheckoutPage
from data.checkout_data import CHECKOUT_DATA
import allure

@allure.title("Verify user can checkout successfully")
def test_checkout_success(add_product_to_cart):
    checkout_page = CheckoutPage(add_product_to_cart)
    
    checkout_page.place_order()
    checkout_page.input_billing_details(
        CHECKOUT_DATA["name"],
        CHECKOUT_DATA["country"],
        CHECKOUT_DATA["city"],
        CHECKOUT_DATA["card_number"],
        CHECKOUT_DATA["month"],
        CHECKOUT_DATA["year"]
    )
    checkout_page.checkout_order()
    
    assert CHECKOUT_DATA["expected_message"] == checkout_page.get_checkout_success_message()
    
    checkout_page.close_success_popup()