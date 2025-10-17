from src.utils.web_helpers.common_imports import By
from src.utils.web_helpers.browser_actions import input_text


def fill_auth_form(browser, name, password):
    input_text(browser, (By.XPATH, "//input[contains(@id, 'username')]"), name, "Ввести имя пользователя")
    input_text(browser, (By.XPATH, "//input[contains(@id, 'password')]"), password, "Ввести пароль")
