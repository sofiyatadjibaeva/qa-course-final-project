from src.utils.web_helpers.browser_actions import click_element
from src.utils.web_helpers.common_imports import allure, By, logging
from src.actions.auth_form import fill_auth_form
from src.actions.checkout import check_checkout_page
from src.actions.navigation import open_main_page, open_cart_page, open_account_page
from src.actions.cart import add_pizza_to_cart


@allure.title("Переход на страницу оформления заказа через корзину")
def test_open_checkout_from_cart(browser):
    logging.info("Start test_open_checkout_from_cart")

    open_main_page(browser)
    add_pizza_to_cart(browser, "425")
    open_account_page(browser)
    fill_auth_form(browser, "rick deckard", "1234")
    click_element(browser, (By.XPATH, "//button[contains(@name, 'login')]"), "Нажать на кнопку «Войти»")
    open_cart_page(browser)
    click_element(browser, (By.XPATH, "//a[contains(@class, 'checkout-button button alt wc-forward')]"),
                  "Нажать на кнопку «Перейти к оплате»")
    check_checkout_page(browser)

    logging.info("Finish test_open_checkout_from_cart")
