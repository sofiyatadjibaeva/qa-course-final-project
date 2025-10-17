from src.utils.web_helpers.common_imports import allure, logging
from src.actions.navigation import open_main_page, open_menu_desserts_section, open_cart_page
from src.actions.cart import add_dessert_to_cart, verify_cart


@allure.title("Добавление десерта в корзину")
def test_add_dessert_to_cart(browser):
    logging.info("Start test_add_dessert_to_cart")

    open_main_page(browser)
    open_menu_desserts_section(browser)
    add_dessert_to_cart(browser, "437")
    open_cart_page(browser)
    cart_items = [
        {"name": "Булочка с корицей", "price": "115,00", "quantity": 1}
    ]
    verify_cart(browser, cart_items)

    logging.info("Finish test_add_dessert_to_cart")
