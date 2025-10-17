from src.utils.web_helpers.common_imports import allure, By, logging
from src.actions.navigation import open_main_page, open_registration_page
from src.utils.web_helpers.browser_actions import click_element, input_text
from src.utils.web_helpers.assertions import assert_text_in_element


@allure.title("Регистрация нового пользователя при пропуске обязательного поля")
def test_register_new_user_with_empty_field(browser):
    logging.info("Start test_register_new_user_with_empty_field")

    open_main_page(browser)
    open_registration_page(browser)
    input_text(browser, (By.XPATH, "//input[contains(@id, 'reg_email')]"), "deckardrick@test.ru", "Ввести адрес почты")
    input_text(browser, (By.XPATH, "//input[contains(@id, 'reg_password')]"), "1234", "Ввести пароль")
    click_element(browser, (By.XPATH, "//button[contains(@name, 'register')]"), "Нажать на кнопку «Зарегистрироваться»")
    assert_text_in_element(browser, (By.XPATH, "//ul[contains(@class, 'woocommerce-error')]/li"),
                           "Пожалуйста введите корректное имя пользователя",
                           "Проверить, что отображается сообщение об ошибке")

    logging.info("Finish test_register_new_user_with_empty_field")
