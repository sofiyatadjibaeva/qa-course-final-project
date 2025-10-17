from src.utils.web_helpers.common_imports import By
from src.utils.web_helpers.assertions import assert_text_in_element, assert_element_visible
from src.utils.web_helpers.browser_actions import input_text


def check_reg_form(browser):
    assert_text_in_element(browser, (By.XPATH, "//h2[contains(@class, 'post-title')]"), "Регистрация",
                           "Проверить, что отображается заголовок «Регистрация»")
    assert_text_in_element(browser, (By.XPATH, "//label[contains(@for, 'reg_username')]"), "Имя пользователя",
                           "Проверить, что отображается соответствующее название поля")
    assert_element_visible(browser, (By.XPATH, "//input[contains(@id, 'reg_username')]"),
                           "Проверить, что отображается поле для ввода имени пользователя")
    assert_text_in_element(browser, (By.XPATH, "//label[contains(@for, 'reg_email')]"), "Адрес почты",
                           "Проверить, что отображается соответствующее название поля")
    assert_element_visible(browser, (By.XPATH, "//input[contains(@id, 'reg_email')]"),
                           "Проверить, что отображается поле для ввода адреса почты")
    assert_text_in_element(browser, (By.XPATH, "//label[contains(@for, 'reg_password')]"), "Пароль",
                           "Проверить, что отображается соответствующее название поля")
    assert_element_visible(browser, (By.XPATH, "//input[contains(@id, 'reg_password')]"),
                           "Проверить, что отображается поле для ввода пароля")
    assert_element_visible(browser, (By.XPATH, "//button[contains(@name, 'register')]"),
                           "Проверить, что отображается кнопка регистрации")


def fill_reg_form(browser, name, email, password):
    input_text(browser, (By.XPATH, "//input[contains(@id, 'reg_username')]"), name, "Ввести имя пользователя")
    input_text(browser, (By.XPATH, "//input[contains(@id, 'reg_email')]"), email, "Ввести адрес почты")
    input_text(browser, (By.XPATH, "//input[contains(@id, 'reg_password')]"), password, "Ввести пароль")
