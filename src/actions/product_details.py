from src.utils.web_helpers.common_imports import By
from src.utils.web_helpers.assertions import assert_text_in_element


def verify_item_details(browser, item_details):

    for item in item_details:
        name = item['name']
        price_str = item['price']

        # Название товара
        assert_text_in_element(
            browser,
            (By.CLASS_NAME, "product_title"),
            name,
            "Проверить название продукта"
        )

        # Цена товара
        assert_text_in_element(
            browser,
            (By.XPATH, "//p[contains(@class, 'price')]//bdi"),
            price_str,
            "Проверить цену продукта"
        )
