from src.utils.web_helpers.browser_actions import click_element, input_text
from src.utils.web_helpers.common_imports import allure, By, logging
from src.actions.auth_form import fill_auth_form
from src.actions.navigation import open_main_page, open_checkout_page, open_account_page
from src.actions.cart import add_pizza_to_cart
from src.utils.web_helpers.assertions import assert_text_in_element


@allure.title("Применение валидного промокода")
def test_apply_valid_promocode(browser):
    logging.info("Start test_apply_valid_promocode")

    open_main_page(browser)
    add_pizza_to_cart(browser, "425")
    open_account_page(browser)
    fill_auth_form(browser, "rick deckard", "1234")
    click_element(browser, (By.XPATH, "//button[contains(@name, 'login')]"), "Нажать на кнопку «Войти»")
    open_checkout_page(browser)
    click_element(browser, (By.XPATH, "//a[contains(@class, 'showcoupon')]"),
                  "Нажать на кнопку «Нажмите для ввода купона»")
    input_text(browser, (By.XPATH, "//input[contains(@id, 'coupon_code')]"), "GIVEMEHALYAVA",
               "Ввести валидный промокод в поле для промокода")
    click_element(browser, (By.XPATH, "//button[contains(@name, 'apply_coupon')]"),
                  "Нажать на кнопку «Применить купон»")
    assert_text_in_element(browser, (By.XPATH, "//div[contains(@class, 'woocommerce-message')]"),
                           "Coupon code applied successfully",
                           "Проверить, что отображается текст в сообщении")
    assert_text_in_element(browser, (By.XPATH, "//tr[contains(@class, 'cart-discount coupon-givemehalyava')]//th"),
                           "Купон: givemehalyava", "Проверить, что отображается текст в сообщении")
    assert_text_in_element(browser, (By.XPATH, "(//span[contains(@class, 'woocommerce-Price-amount amount')])[3]"),
                           "43,50", "Проверить, что отображается текст в сообщении")
    assert_text_in_element(browser, (By.XPATH, "(//span[contains(@class, 'woocommerce-Price-amount amount')]//bdi)[3]"),
                           "391,50", "Проверить, что отображается текст в сообщении")

    logging.info("Finish test_apply_valid_promocode")
