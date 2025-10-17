from src.utils.web_helpers.common_imports import By
from src.utils.web_helpers.assertions import assert_text_in_element, assert_element_visible
from src.utils.web_helpers.browser_actions import input_text


def check_checkout_page(browser):
    assert_text_in_element(browser, (By.XPATH, "//h2[contains(@class, 'post-title')]"),
                           "Оформление заказа", "Проверить, что отображается заголовок «Оформление заказа»")

    assert_text_in_element(browser, (By.XPATH, "(//h3)[1]"), "Детали заказа",
                           "Проверить, что отображается подзаголовок «Детали заказа»")

    assert_text_in_element(browser, (By.XPATH, "//label[contains(@for, 'billing_first_name')]"), "Имя",
                           "Проверить, что отображается соответствующее название поля")
    assert_element_visible(browser, (By.XPATH, "//input[contains(@id, 'billing_first_name')]"),
                           "Проверить, что отображается поле для ввода имени пользователя")

    assert_text_in_element(browser, (By.XPATH, "//label[contains(@for, 'billing_last_name')]"), "Фамилия",
                           "Проверить, что отображается соответствующее название поля")
    assert_element_visible(browser, (By.XPATH, "//input[contains(@id, 'billing_last_name')]"),
                           "Проверить, что отображается поле для ввода фамилии пользователя")

    assert_text_in_element(browser, (By.XPATH, "//label[contains(@for, 'billing_country')]"), "Страна / Регион",
                           "Проверить, что отображается соответствующее название поля")
    assert_element_visible(browser, (By.XPATH, "//span[contains(@id, 'select2-billing_country-container')]"),
                           "Проверить, что отображается селектор со странами")

    assert_text_in_element(browser, (By.XPATH, "//label[contains(@for, 'billing_address_1')]"), "Адрес",
                           "Проверить, что отображается соответствующее название поля")
    assert_element_visible(browser, (By.XPATH, "//input[contains(@id, 'billing_address_1')]"),
                           "Проверить, что отображается поле для ввода адреса пользователя")

    assert_text_in_element(browser, (By.XPATH, "//label[contains(@for, 'billing_city')]"), "Город / Населенный пункт",
                           "Проверить, что отображается соответствующее название поля")
    assert_element_visible(browser, (By.XPATH, "//input[contains(@id, 'billing_city')]"),
                           "Проверить, что отображается поле для ввода города пользователя")

    assert_text_in_element(browser, (By.XPATH, "//label[contains(@for, 'billing_state')]"), "Область",
                           "Проверить, что отображается соответствующее название поля")
    assert_element_visible(browser, (By.XPATH, "//input[contains(@id, 'billing_state')]"),
                           "Проверить, что отображается поле для ввода области пользователя")

    assert_text_in_element(browser, (By.XPATH, "//label[contains(@for, 'billing_postcode')]"), "Почтовый индекс",
                           "Проверить, что отображается соответствующее название поля")
    assert_element_visible(browser, (By.XPATH, "//input[contains(@id, 'billing_postcode')]"),
                           "Проверить, что отображается поле для ввода почтового индекса пользователя")

    assert_text_in_element(browser, (By.XPATH, "//label[contains(@for, 'billing_phone')]"), "Телефон",
                           "Проверить, что отображается соответствующее название поля")
    assert_element_visible(browser, (By.XPATH, "//input[contains(@id, 'billing_phone')]"),
                           "Проверить, что отображается поле для ввода номера телефона пользователя")

    assert_text_in_element(browser, (By.XPATH, "//label[contains(@for, 'billing_email')]"), "Адрес почты",
                           "Проверить, что отображается соответствующее название поля")
    assert_element_visible(browser, (By.XPATH, "//input[contains(@id, 'billing_email')]"),
                           "Проверить, что отображается поле для ввода адреса почты")

    assert_text_in_element(browser, (By.XPATH, "(//h3)[2]"), "Дополнительная информация",
                           "Проверить, что отображается подзаголовок «Дополнительная информация»")

    assert_text_in_element(browser, (By.XPATH, "//label[contains(@for, 'order_date')]"), "Дата заказа",
                           "Проверить, что отображается соответствующее название поля")
    assert_element_visible(browser, (By.XPATH, "//input[contains(@id, 'order_date')]"),
                           "Проверить, что отображается поле для ввода даты заказа")

    assert_text_in_element(browser, (By.XPATH, "//label[contains(@for, 'order_comments')]"), "Комментарии к заказу",
                           "Проверить, что отображается соответствующее название поля")
    assert_element_visible(browser, (By.XPATH, "//textarea[contains(@id, 'order_comments')]"),
                           "Проверить, что отображается поле для ввода комментария")

    assert_text_in_element(browser, (By.XPATH, "//h3[contains(@id, 'order_review_heading')]"), "Ваш заказ",
                           "Проверить, что отображается подзаголовок «Ваш заказ»")

    assert_text_in_element(browser, (By.XPATH, "//th[contains(@class, 'product-name')]"), "Товар",
                           "Проверить, что отображается название ячейки «Товар»")
    assert_text_in_element(browser, (By.XPATH, "//th[contains(@class, 'product-total')]"), "Общая стоимость",
                           "Проверить, что отображается название ячейки «Общая стоимость»")
    assert_text_in_element(browser, (By.XPATH, "//tr[contains(@class, 'order-total')]//th"), "Сумма",
                           "Проверить, что отображается название ячейки «Сумма»")

    assert_text_in_element(browser, (By.XPATH, "//label[contains(@for, 'payment_method_bacs')]"),
                           "Прямой банковский перевод",
                           "Проверить, что отображается соответствующее название радиобаттона")
    assert_element_visible(browser, (By.XPATH, "//input[contains(@id, 'payment_method_bacs')]"),
                           "Проверить, что отображается радиобаттон метода доставки")

    assert_text_in_element(browser, (By.XPATH, "//label[contains(@for, 'payment_method_cod')]"), "Оплата при доставке",
                           "Проверить, что отображается соответствующее название радиобаттона")
    assert_element_visible(browser, (By.XPATH, "//input[contains(@id, 'payment_method_cod')]"),
                           "Проверить, что отображается радиобаттон метода доставки")

    assert_text_in_element(browser, (By.XPATH, "(//input[contains(@id, 'terms')]/following-sibling::span)[1]"),
                           "I have read and agree to the website terms and conditions",
                           "Проверить, что отображается соответствующее название радиобаттона")
    assert_element_visible(browser, (By.XPATH, "//input[contains(@id, 'terms')]"),
                           "Проверить, что отображается чекбокс terms and conditions")

    assert_element_visible(browser, (By.XPATH, "//button[contains(@name, 'woocommerce_checkout_place_order')]"),
                           "Проверить, что отображается кнопка оформления заказа")


def fill_checkout(browser, name, last_name, address, city, state, postcode, phone):
    input_text(browser, (By.XPATH, "//input[contains(@id, 'billing_first_name')]"), name, "Ввести имя пользователя")
    input_text(browser, (By.XPATH, "//input[contains(@id, 'billing_last_name')]"), last_name, "Ввести фамилию")
    input_text(browser, (By.XPATH, "//input[contains(@id, 'billing_address_1')]"), address, "Ввести адрес")
    input_text(browser, (By.XPATH, "//input[contains(@id, 'billing_city')]"), city, "Ввести название города")
    input_text(browser, (By.XPATH, "//input[contains(@id, 'billing_state')]"), state, "Ввести название области")
    input_text(browser, (By.XPATH, "//input[contains(@id, 'billing_postcode')]"), postcode, "Ввести почтовый индекс")
    input_text(browser, (By.XPATH, "//input[contains(@id, 'billing_phone')]"), phone, "Ввести номер телефона")
