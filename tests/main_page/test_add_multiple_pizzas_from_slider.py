from src.utils.web_helpers.common_imports import allure, logging
from src.actions.cart import add_pizza_to_cart, verify_cart
from src.actions.navigation import open_main_page, open_cart_page


@allure.title("Добавление нескольких пицц в корзину через слайдер")
def test_add_multiple_pizzas_from_slider(browser):
    logging.info("Start test_add_multiple_pizzas_from_slider")

    open_main_page(browser)
    add_pizza_to_cart(browser, "425")
    add_pizza_to_cart(browser, "423")
    open_cart_page(browser)
    cart_items = [
        {"name": "4 в 1", "price": "435,00", "quantity": 1},
        {"name": "Как у бабушки", "price": "480,00", "quantity": 1}
    ]

    verify_cart(browser, cart_items)

    logging.info("Finish test_add_multiple_pizzas_from_slider")
