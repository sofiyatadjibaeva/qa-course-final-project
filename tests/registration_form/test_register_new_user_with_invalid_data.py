from src.utils.web_helpers.common_imports import allure, By, logging
from src.actions.navigation import open_main_page, open_registration_page
from src.actions.reg_form import fill_reg_form
from src.utils.web_helpers.browser_actions import click_element
from src.utils.web_helpers.assertions import assert_text_in_element


@allure.title("Регистрация нового пользователя при вводе невалидных данных")
def test_register_new_user_with_invalid_data(browser):
    logging.info("Start test_register_new_user_with_invalid_data")

    open_main_page(browser)
    open_registration_page(browser)
    fill_reg_form(browser, "!!!.$", "deckk@gmail.com", "1")
    click_element(browser, (By.XPATH, "//button[contains(@name, 'register')]"), "Нажать на кнопку «Зарегистрироваться»")
    assert_text_in_element(browser, (By.XPATH, "//ul[contains(@class, 'woocommerce-error')]/li"),
                           "Пожалуйста введите корректное имя пользователя",
                           "Проверить, что отображается сообщение об ошибке")
    fill_reg_form(browser, "winston smith", "toolongggg@gmaill.commmm", "1")
    click_element(browser, (By.XPATH, "//button[contains(@name, 'register')]"), "Нажать на кнопку «Зарегистрироваться»")
    assert_text_in_element(browser, (By.XPATH, "//ul[contains(@class, 'woocommerce-error')]/li"),
                           "Максимальное допустимое количество символов: 20",
                           "Проверить, что отображается сообщение об ошибке")

    logging.info("Finish test_register_new_user_with_invalid_data")
