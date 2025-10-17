from src.utils.web_helpers.common_imports import allure, By, logging
from src.actions.navigation import open_main_page
from src.utils.web_helpers.assertions import assert_text_in_element


@allure.title("Открытие главной страницы сайта")
def test_open_main_page(browser):
    logging.info("Start test_open_main_pagee")

    open_main_page(browser)

    assert_text_in_element(browser, (By.CLASS_NAME, "site-title"), "Pizzeria", "Проверить заголовок главной страницы")

    body = browser.find_element(By.TAG_NAME, "body")
    assert body.is_displayed(), "Главная страница не загрузилась"

    assert browser.title == "Pizzeria — Пиццерия"

    logging.info("Finish test_open_main_page")
