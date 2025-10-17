from src.utils.web_helpers.browser_actions import click_element, move_to_element
from src.utils.web_helpers.common_imports import allure, By, logging
from src.actions.navigation import open_main_page


@allure.title("Переключение слайдера на главной странице")
def test_slider_navigation(browser):
    logging.info("Start test_slider_navigation")

    open_main_page(browser)
    move_to_element(browser, (By.XPATH, "(//ul[contains(@class, 'slick-initialized')])[1]"),
                    "Навести курсор на слайдер")
    click_element(browser, (By.CLASS_NAME, "slick-next"), "Нажать на правый переключатель слайдера")
    slide_locator = (By.XPATH, "(//aside[@id='accesspress_store_product-5']//li[contains(@class,'slick-slide')])[5]")
    slide_next = browser.find_element(*slide_locator)
    classes = slide_next.get_attribute("class").split()
    assert "slick-active" not in classes

    click_element(browser, (By.CLASS_NAME, "slick-prev"), "Нажать на левый переключатель слайдера")
    slide_prev = browser.find_element(*slide_locator)
    classes = slide_prev.get_attribute("class").split()
    assert "slick-active" in classes

    logging.info("Finish test_slider_navigation")
