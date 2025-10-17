from src.utils.web_helpers.browser_actions import click_element
from src.utils.web_helpers.common_imports import allure, By, logging
from src.actions.navigation import open_main_page, open_account_page
from src.actions.reg_form import check_reg_form


@allure.title("Переход на страницу с формой регистрации через вкладку «Мой аккаунт» в навигационном меню")
def test_open_registration_via_my_account(browser):
    logging.info("Start test_open_registration_via_my_account")

    open_main_page(browser)
    open_account_page(browser)
    click_element(browser, (By.XPATH, "//button[contains(@class, 'custom-register-button')]"),
                  "Нажать на кнопку «Зарегистрироваться»")
    check_reg_form(browser)

    logging.info("Finish test_open_registration_via_my_account")
