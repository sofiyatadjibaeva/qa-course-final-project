from src.utils.web_helpers.browser_actions import click_element
from src.utils.web_helpers.common_imports import allure, By, logging
from src.actions.auth_form import fill_auth_form
from src.actions.checkout import fill_checkout
from src.actions.navigation import open_main_page, open_checkout_page, open_account_page
from src.actions.cart import add_pizza_to_cart
from src.utils.web_helpers.assertions import assert_text_in_element


@allure.title("Оформление заказа при вводе валидных данных")
def test_register_new_user_with_valid_data(browser):
    logging.info("Start test_register_new_user_with_valid_data")

    open_main_page(browser)
    add_pizza_to_cart(browser, "425")
    open_account_page(browser)
    fill_auth_form(browser, "rick deckard", "1234")
    click_element(browser, (By.XPATH, "//button[contains(@name, 'login')]"), "Нажать на кнопку «Войти»")
    open_checkout_page(browser)
    fill_checkout(browser, "Рик", "Декард", "Ул Ленина дом 122", "Москва", "Московская", "123456", "79221110500")
    click_element(browser, (By.XPATH, "//input[contains(@id, 'terms')]"), "Нажать на чекбокс terms and conditions")
    click_element(browser, (By.XPATH, "//button[contains(@id, 'place_order')]"), "Нажать на кнопку «Оформить заказ»")
    assert_text_in_element(browser, (By.XPATH, "//h2[contains(@class, 'post-title')]"), "Заказ получен",
                           "Проверить, что отображается заголовок «Заказ получен»")

    logging.info("Finish test_register_new_user_with_valid_data")
