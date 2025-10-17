from src.utils.web_helpers.common_imports import By
from src.utils.web_helpers.assertions import assert_text_in_element
from src.utils.web_helpers.browser_actions import click_element, move_to_element


def add_pizza_to_cart(browser, product_id):
    move_to_element(browser,
                    (By.XPATH, f"//a[@data-product_id='{product_id}']/ancestor::div[contains(@class,'item-img')]"),
                    f"Навести курсор на пиццу с ID {product_id}")
    click_element(browser, (By.XPATH, f"//a[@data-product_id='{product_id}']"),
                  f"Нажать на кнопку «В корзину» для пиццы с ID {product_id}")


def add_dessert_to_cart(browser, product_id):
    click_element(browser, (By.XPATH, f"//a[@data-product_id='{product_id}']"),
                  f"Нажать на кнопку «В корзину» для десерта с ID {product_id}")


def verify_cart(browser, cart_items):
    total_sum = 0.0

    for item in cart_items:
        name = item['name']
        price_str = item['price']
        price = float(price_str.replace(",", "."))
        quantity = item.get('quantity', 1)
        subtotal = price * quantity
        subtotal_str = f"{subtotal:.2f}".replace(".", ",")

        total_sum += subtotal

        # Название продукта
        assert_text_in_element(
            browser,
            (By.XPATH, f"//td//a[contains(text(), '{name}')]"),
            name,
            "Проверить название продукта"
        )

        # Цена продукта
        assert_text_in_element(
            browser,
            (By.XPATH, f"//td[contains(@class, 'product-price')]//bdi[text()='{price_str}']"),
            price_str,
            "Проверить цену продукта"
        )

        # Подитог
        assert_text_in_element(
            browser,
            (By.XPATH, f"//td[contains(@class, 'product-subtotal')]//bdi[text()='{subtotal_str}']"),
            subtotal_str,
            "Проверить подитог продукта)"
        )

    # Итоговая сумма заказа
    total_str = f"{total_sum:.2f}".replace(".", ",")
    assert_text_in_element(
        browser,
        (By.XPATH, "//tr[contains(@class, 'order-total')]//bdi"),
        total_str,
        "Проверить итоговую сумму заказа"
    )
