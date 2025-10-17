from src.utils.web_helpers.browser_actions import click_element
from src.utils.web_helpers.common_imports import allure, By, logging
from src.actions.navigation import open_main_page, open_loyalty_program_page
from src.utils.web_helpers.assertions import assert_text_in_element


@allure.title("Регистрация в бонусной программе при пропуске обязательного поля")
def test_register_in_loyalty_program_with_empty_field(browser):
    logging.info("Start test_register_in_loyalty_program_with_empty_field")

    open_main_page(browser)
    open_loyalty_program_page(browser)
    click_element(browser, (By.XPATH, "//button[contains(@name, 'bonus')]"), "Нажать на кнопку  «Оформить карту»")
    assert_text_in_element(browser, (By.XPATH, "//div[contains(@id, 'bonus_content')]"),
                           'Поле "Имя" обязательно для заполнения Поле "Телефон" обязательно для заполнения',
                           "Проверить, что отображается текст")

    logging.info("Finish test_register_in_loyalty_program_with_empty_field")
