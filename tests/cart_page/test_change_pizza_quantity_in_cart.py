from src.utils.web_helpers.common_imports import allure, By, logging
from src.actions.cart import add_pizza_to_cart, verify_cart
from src.actions.navigation import open_main_page, open_cart_page
from src.utils.web_helpers.browser_actions import input_text, click_element


@allure.title("Изменение количества пиццы в корзине")
def test_change_pizza_quantity_in_cart(browser):
    logging.info("Start test_change_pizza_quantity_in_cart")

    open_main_page(browser)
    add_pizza_to_cart(browser, "425")
    open_cart_page(browser)
    qty_input = browser.find_element(By.XPATH, "//input[contains(@class, 'input-text qty text')]")
    current_value = qty_input.get_attribute("value")
    print("Текущее количество:", current_value)
    input_text(browser, (By.XPATH, "//input[contains(@class, 'input-text qty text')]"), "2",
               "Ввести число в поле количества")
    click_element(browser, (By.XPATH, "//button[contains(text(), 'Обновить корзину')]"),
                  "Нажать на кнопку «Обновить корзину»")
    qty_input = browser.find_element(By.XPATH, "//input[contains(@class, 'input-text qty text')]")
    new_value = qty_input.get_attribute("value")
    assert new_value == "2"
    cart_items = [
        {"name": "4 в 1", "price": "435,00", "quantity": 2}
    ]
    verify_cart(browser, cart_items)

    logging.info("Finish test_change_pizza_quantity_in_cart")
