from src.utils.web_helpers.browser_actions import click_element
from src.utils.web_helpers.common_imports import allure, By, logging
from src.actions.navigation import open_main_page
from src.actions.product_details import verify_item_details


@allure.title("Переход на страницу с описанием пиццы")
def test_open_pizza_page_from_main(browser):
    logging.info("Start test_open_pizza_page_from_main")

    open_main_page(browser)
    click_element(browser, (By.XPATH,
                  "(//aside[@id='accesspress_store_product-5']//li[contains(@class,'slick-active')])[1]"),
                  "Нажать на изображение пиццы")
    item_details = [
        {"name": "4 в 1", "price": "435,00"}
    ]

    verify_item_details(browser, item_details)

    logging.info("Finish test_open_pizza_page_from_main")
