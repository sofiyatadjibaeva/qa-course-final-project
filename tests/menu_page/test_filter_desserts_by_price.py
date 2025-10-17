from src.utils.web_helpers.browser_actions import click_element, move_slider
from src.utils.web_helpers.common_imports import allure, By, logging
from src.actions.navigation import open_main_page, open_menu_desserts_section


@allure.title("Фильтрация десертов по цене")
def test_filter_desserts_by_price(browser):
    logging.info("Start test_filter_desserts_by_price")

    open_main_page(browser)
    open_menu_desserts_section(browser)
    move_slider(browser, (By.XPATH, "(//span[contains(@class, 'ui-slider-handle ui-state-default ui-corner-all')])[2]"),
                -500, "Потянуть ползунок до значения 130")
    click_element(browser, (By.XPATH, "//button[contains(text(), 'Применить')]"), "Нажать на кнопку «Применить»")
    prices = browser.find_elements(By.XPATH, "//div[contains(@class, 'price-cart')]//bdi")
    for price in prices:
        raw_text = price.text.replace("₽", "").strip()
        value = float(raw_text.replace(",", "."))
        assert value <= 130.0

    logging.info("Finish test_filter_desserts_by_price")
