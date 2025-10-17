from src.utils.web_helpers.common_imports import allure, logging
from src.actions.navigation import open_main_page, open_registration_page
from src.actions.reg_form import check_reg_form


@allure.title("Переход на страницу с формой регистрации через ссылку «Регистрация» в футере")
def test_open_registration_via_footer(browser):
    logging.info("Start test_open_registration_via_footer")

    open_main_page(browser)
    open_registration_page(browser)
    check_reg_form(browser)

    logging.info("Finish test_open_registration_via_footer")
