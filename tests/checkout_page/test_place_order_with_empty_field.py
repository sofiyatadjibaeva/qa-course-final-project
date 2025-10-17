from src.utils.web_helpers.browser_actions import click_element
from src.utils.web_helpers.common_imports import allure, By, logging
from src.actions.auth_form import fill_auth_form
from src.actions.navigation import open_main_page, open_checkout_page, open_account_page
from src.actions.cart import add_pizza_to_cart
from src.utils.web_helpers.assertions import assert_text_in_element


@allure.title("Попытка оформить заказ при пропуске ввода данных в обязательное поле")
def test_place_order_with_empty_field(browser):
    logging.info("Start test_place_order_with_empty_field")

    open_main_page(browser)
    add_pizza_to_cart(browser, "425")
    open_account_page(browser)
    fill_auth_form(browser, "rick deckard", "1234")
    click_element(browser, (By.XPATH, "//button[contains(@name, 'login')]"), "Нажать на кнопку «Войти»")
    open_checkout_page(browser)
    click_element(browser, (By.XPATH, "//button[contains(@id, 'place_order')]"), "Нажать на кнопку «Оформить заказ»")
    assert_text_in_element(browser, (By.XPATH, "//li[contains(@data-id, 'billing_first_name')]"),
                           "Имя для выставления счета обязательное поле",
                           "Проверить, что отображается текст в сообщении")
    assert_text_in_element(browser, (By.XPATH, "//li[contains(@data-id, 'billing_last_name')]"),
                           "Фамилия для выставления счета обязательное поле",
                           "Проверить, что отображается текст в сообщении")
    assert_text_in_element(browser, (By.XPATH, "//li[contains(@data-id, 'billing_address_1')]"),
                           "Адрес для выставления счета обязательное поле",
                           "Проверить, что отображается текст в сообщении")
    assert_text_in_element(browser, (By.XPATH, "//li[contains(@data-id, 'billing_city')]"),
                           "Город / Населенный пункт для выставления счета обязательное поле",
                           "Проверить, что отображается текст в сообщении")
    assert_text_in_element(browser, (By.XPATH, "//li[contains(@data-id, 'billing_state')]"),
                           "Область для выставления счета обязательное поле",
                           "Проверить, что отображается текст в сообщении")
    assert_text_in_element(browser, (By.XPATH, "//li[contains(@data-id, 'billing_postcode')]"),
                           "Почтовый индекс для выставления счета обязательное поле",
                           "Проверить, что отображается текст в сообщении")
    assert_text_in_element(browser, (By.XPATH, "(//li[contains(@data-id, 'billing_phone')])[2]"),
                           "Телефон для выставления счета обязательное поле",
                           "Проверить, что отображается текст в сообщении")

    logging.info("Finish test_place_order_with_empty_field")
