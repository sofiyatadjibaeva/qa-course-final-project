from src.utils.web_helpers.browser_actions import click_element
from src.utils.web_helpers.common_imports import allure, By, logging
from src.actions.navigation import open_main_page


@allure.title("Переход на страницу корзины через навигационное меню")
def test_open_cart_via_more_button_from_product_page(browser):
    logging.info("Start test_open_cart_via_more_button_from_product_page")

    open_main_page(browser)
    click_element(browser, (By.XPATH,
                  "(//aside[@id='accesspress_store_product-5']//li[contains(@class,'slick-active')])[1]"),
                  "Нажать на изображение пиццы")
    click_element(browser, (By.XPATH, "//button[@name='add-to-cart']"), "Нажать на кнопку «В корзину»")
    click_element(browser, (By.XPATH, "//a[contains(text(), 'Подробнее')]"), "Нажать на кнопку «Подробнее»")
    body = browser.find_element(By.TAG_NAME, "body")
    assert body.is_displayed(), "Страница корзины не загрузилась"
    assert browser.title == "Корзина — Pizzeria"
    assert "cart" in browser.current_url

    logging.info("Finish test_open_cart_via_more_button_from_product_page")
