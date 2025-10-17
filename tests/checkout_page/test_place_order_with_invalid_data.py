from src.utils.web_helpers.browser_actions import click_element
from src.utils.web_helpers.common_imports import allure, By, logging
from src.actions.auth_form import fill_auth_form
from src.actions.checkout import fill_checkout
from src.actions.navigation import open_main_page, open_checkout_page, open_account_page
from src.actions.cart import add_pizza_to_cart
from src.utils.web_helpers.assertions import assert_text_in_element


@allure.title("Попытка оформить заказ при вводе невалидных данных")
def test_place_order_with_invalid_data(browser):
    logging.info("Start test_place_order_with_invalid_data")

    open_main_page(browser)
    add_pizza_to_cart(browser, "425")
    open_account_page(browser)
    fill_auth_form(browser, "rick deckard", "1234")
    click_element(browser, (By.XPATH, "//button[contains(@name, 'login')]"), "Нажать на кнопку «Войти»")
    open_checkout_page(browser)
    fill_checkout(browser, "##@#112", "##@#112", "@#@!", "@#@!", "@#@!", "123", "телефон")
    click_element(browser, (By.XPATH, "//button[contains(@id, 'place_order')]"), "Нажать на кнопку «Оформить заказ»")
    assert_text_in_element(browser, (By.XPATH, "//li[contains(@data-id, 'billing_first_name')]"),
                           "не валидный",
                           "Проверить, что отображается текст в сообщении")
    assert_text_in_element(browser, (By.XPATH, "//li[contains(@data-id, 'billing_last_name')]"),
                           "не валидный",
                           "Проверить, что отображается текст в сообщении")
    assert_text_in_element(browser, (By.XPATH, "//li[contains(@data-id, 'billing_address_1')]"),
                           "не валидный",
                           "Проверить, что отображается текст в сообщении")
    assert_text_in_element(browser, (By.XPATH, "//li[contains(@data-id, 'billing_city')]"),
                           "не валидный",
                           "Проверить, что отображается текст в сообщении")
    assert_text_in_element(browser, (By.XPATH, "//li[contains(@data-id, 'billing_state')]"),
                           "не валидный",
                           "Проверить, что отображается текст в сообщении")
    assert_text_in_element(browser, (By.XPATH, "//li[contains(@data-id, 'billing_postcode')]"),
                           "не валидный",
                           "Проверить, что отображается текст в сообщении")
    assert_text_in_element(browser, (By.XPATH, "(//li[contains(@data-id, 'billing_phone')])[1]"),
                           "Телефон для выставления счета не валидный номер телефона",
                           "Проверить, что отображается текст в сообщении")

    logging.info("Finish test_place_order_with_invalid_data")
