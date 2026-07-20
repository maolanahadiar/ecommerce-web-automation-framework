import allure
from pages.checkout_page import CheckoutPage
from testdata.billing import BILLING_INFO

@allure.title("Verify user can checkout successfully")
def test_checkout_success(add_product_to_cart):
    checkout_page = CheckoutPage(add_product_to_cart)
    
    checkout_page.place_order()
    checkout_page.input_billing_details(
        BILLING_INFO["name"],
        BILLING_INFO["country"],
        BILLING_INFO["city"],
        BILLING_INFO["card_number"],
        BILLING_INFO["month"],
        BILLING_INFO["year"]
    )
    checkout_page.checkout_order()
    
    assert checkout_page.get_checkout_success_message() == BILLING_INFO["expected_message"]
    
    checkout_page.close_success_popup()