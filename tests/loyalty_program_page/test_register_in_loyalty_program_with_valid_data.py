from src.utils.web_helpers.browser_actions import click_element
from src.utils.web_helpers.common_imports import By, logging, allure, WebDriverWait, EC
from src.actions.loyalty_program import fill_loyalty_program_reg_form
from src.actions.navigation import open_main_page, open_loyalty_program_page
from src.utils.web_helpers.assertions import assert_text_in_element


@allure.title("Регистрация в бонусной программе при вводе валидных данных")
def test_register_in_loyalty_program_with_valid_data(browser):
    logging.info("Start test_register_in_loyalty_program_with_valid_data")

    open_main_page(browser)
    open_loyalty_program_page(browser)
    fill_loyalty_program_reg_form(browser, "Rick", "79221110500")
    click_element(browser, (By.XPATH, "//button[contains(@name, 'bonus')]"), "Нажать на кнопку  «Оформить карту»")
    wait = WebDriverWait(browser, 10)
    alert = wait.until(EC.alert_is_present())
    assert "Заявка отправлена" in alert.text
    alert.accept()
    assert_text_in_element(browser, (By.XPATH, "//div[contains(@id, 'bonus_main')]//h3"), "Ваша карта оформлена!",
                           "Проверить, что отображается текст")
    assert_text_in_element(browser, (By.XPATH, "//div[contains(@id, 'bonus_main')]"),
                           "Для применения скидки укажите номер телефона владельца карты в комментариях к заказу",
                           "Проверить, что отображается текст")

    logging.info("Finish test_register_in_loyalty_program_with_valid_data")
