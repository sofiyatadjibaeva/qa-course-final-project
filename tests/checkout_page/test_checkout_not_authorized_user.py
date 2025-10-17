from src.utils.web_helpers.common_imports import allure, By, logging
from src.actions.navigation import open_main_page, open_checkout_page
from src.actions.cart import add_pizza_to_cart
from src.utils.web_helpers.assertions import assert_text_in_element


@allure.title("Попытка оформить заказ неавторизованным пользователем")
def test_checkout_not_authorized_user(browser):
    logging.info("Start test_checkout_not_authorized_user")

    open_main_page(browser)
    add_pizza_to_cart(browser, "425")
    open_checkout_page(browser)
    assert_text_in_element(browser, (By.XPATH, "(//div[contains(@class, 'woocommerce-info')])[1]"),
                           "Зарегистрированы на сайте?", "Проверить, что отображается текст в сообщении")
    assert_text_in_element(browser, (By.CLASS_NAME, "showlogin"), "Авторизуйтесь",
                           "Проверить, что отображается текст в сообщении")

    logging.info("Finish test_checkout_not_authorized_user")
