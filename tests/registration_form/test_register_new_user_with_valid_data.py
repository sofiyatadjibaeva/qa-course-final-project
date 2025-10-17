from selenium.webdriver.common.by import By
from src.utils.web_helpers.common_imports import allure, logging
from src.actions.navigation import open_main_page, open_registration_page
from src.actions.reg_form import fill_reg_form
from src.utils.web_helpers.browser_actions import click_element
from src.utils.web_helpers.assertions import assert_text_in_element


@allure.title("Регистрация нового пользователя при вводе валидных данных")
def test_register_new_user_with_valid_data(browser):
    logging.info("Start test_register_new_user_with_valid_data")

    open_main_page(browser)
    open_registration_page(browser)
    fill_reg_form(browser, "rick deckard", "deckard@gmail.com", "1234")
    click_element(browser, (By.XPATH, "//button[contains(@name, 'register')]"), "Нажать на кнопку «Зарегистрироваться»")
    assert_text_in_element(browser, (By.XPATH, "//div[contains(@class, 'content-page')]//div"), "Регистрация завершена",
                           "Проверить, что отображается сообщение об успешной регистрации")

    logging.info("Finish test_register_new_user_with_valid_data")
