from src.utils.web_helpers.common_imports import allure, By, logging
from src.actions.cart import add_pizza_to_cart
from src.actions.navigation import open_main_page, open_cart_page
from src.utils.web_helpers.browser_actions import click_element, wait_for_element
from src.utils.web_helpers.assertions import assert_text_in_element


@allure.title("Удаление пиццы из корзины")
def test_delete_pizza_from_cart(browser):
    logging.info("Start test_delete_pizza_from_cart")

    open_main_page(browser)
    add_pizza_to_cart(browser, "425")
    open_cart_page(browser)
    click_element(browser, (By.XPATH, "//td//a[contains(@class, 'remove')]"), "Нажать на кнопку удаления")
    wait_for_element(browser, (By.XPATH, "//p[contains(@class, 'cart-empty woocommerce-info')]"),
                     "Дождаться сообщения о пустой корзине", 30)
    assert_text_in_element(browser, (By.XPATH, "//p[contains(@class, 'cart-empty woocommerce-info')]"), "Корзина пуста",
                           "Проверить сообщение")

    logging.info("Finish test_delete_pizza_from_cart")
