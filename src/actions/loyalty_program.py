from src.utils.web_helpers.common_imports import By
from src.utils.web_helpers.browser_actions import input_text


def fill_loyalty_program_reg_form(browser, name, phone):
    input_text(browser, (By.XPATH, "//input[contains(@id, 'username')]"), name, "Ввести имя пользователя")
    input_text(browser, (By.XPATH, "//input[contains(@id, 'bonus_phone')]"), phone, "Ввести номер телефона")
