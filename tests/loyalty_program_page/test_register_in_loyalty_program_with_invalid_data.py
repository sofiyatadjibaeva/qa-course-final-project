from src.utils.web_helpers.browser_actions import click_element
from src.utils.web_helpers.common_imports import allure, By, logging
from src.actions.loyalty_program import fill_loyalty_program_reg_form
from src.actions.navigation import open_main_page, open_loyalty_program_page
from src.utils.web_helpers.assertions import assert_text_in_element


@allure.title("Регистрация в бонусной программе при вводе невалидных данных")
def test_register_in_loyalty_program_with_invalid_data(browser):
    logging.info("Start test_register_in_loyalty_program_with_invalid_data")

    open_main_page(browser)
    open_loyalty_program_page(browser)
    fill_loyalty_program_reg_form(browser, " ", "телефон")
    click_element(browser, (By.XPATH, "//button[contains(@name, 'bonus')]"), "Нажать на кнопку  «Оформить карту»")
    assert_text_in_element(browser, (By.XPATH, "//div[contains(@id, 'bonus_content')]"),
                           "Введен неверный формат телефона", "Проверить, что отображается текст")

    logging.info("Finish test_register_in_loyalty_program_with_invalid_data")
