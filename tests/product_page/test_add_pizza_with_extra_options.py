from src.utils.web_helpers.browser_actions import click_element
from src.utils.web_helpers.common_imports import allure, By, logging
from src.actions.navigation import open_main_page, open_cart_page
from src.actions.cart import verify_cart
from src.actions.product_details import verify_item_details


@allure.title("Добавление пиццы с доп. опциями")
def test_add_pizza_with_extra_options(browser):
    logging.info("Start test_add_pizza_with_extra_options")

    open_main_page(browser)
    click_element(browser, (By.XPATH,
                  "(//aside[@id='accesspress_store_product-5']//li[contains(@class,'slick-active')])[1]"),
                  "Нажать на изображение пиццы")
    click_element(browser, (By.NAME, "board_pack"), "Нажать на селектор доп.опций")
    click_element(browser, (By.XPATH, "//option[contains(text(), 'Сырный')]"), "Выбрать сырный борт для пиццы")
    item_details = [
        {"name": "4 в 1", "price": "490,00"}
    ]
    verify_item_details(browser, item_details)
    open_cart_page(browser)
    cart_items = [
        {"name": "4 в 1", "price": "490,00", "quantity": 1},
    ]

    verify_cart(browser, cart_items)
