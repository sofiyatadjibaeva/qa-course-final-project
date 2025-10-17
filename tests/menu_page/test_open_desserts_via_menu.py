from src.utils.web_helpers.common_imports import allure, By, logging
from src.actions.navigation import open_main_page, open_menu_desserts_section


@allure.title("Переход в раздел «Десерты» через вкладку «Меню»")
def test_open_desserts_via_menu(browser):
    logging.info("Start test_open_desserts_via_menu")

    open_main_page(browser)
    open_menu_desserts_section(browser)
    body = browser.find_element(By.TAG_NAME, "body")
    assert body.is_displayed(), "Страница раздела с десертами  не загрузилась"
    assert browser.title == "Десерты — Pizzeria"
    assert "deserts" in browser.current_url

    logging.info("Finish test_open_desserts_via_menu")
