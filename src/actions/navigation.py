from src.utils.web_helpers.browser_actions import open_page, click_element, move_to_element
from src.utils.web_helpers.common_imports import By


def open_main_page(browser):
    url = "https://pizzeria.skillbox.cc/"
    open_page(browser, url, "Открыть главную страницу сайта Pizzeria")


def open_cart_page(browser):
    click_element(browser, (By.XPATH, "//a[contains(text(), 'Корзина')]"), "Открыть страницу корзины")


def open_checkout_page(browser):
    click_element(browser, (By.XPATH, "//a[contains(text(), 'Оформление заказа')]"),
                  "Открыть страницу оформления заказа")


def open_account_page(browser):
    click_element(browser, (By.XPATH, "//a[contains(text(), 'Мой аккаунт')]"),
                  "Открыть страницу аккаунта")


def open_registration_page(browser):
    click_element(browser, (By.XPATH, "//a[contains(text(), 'Регистрация')]"),
                  "Открыть страницу с формой регистрации")


def open_auth_page(browser):
    click_element(browser, (By.XPATH, "//header//*[contains(text(), 'Войти')]"),
                  "Открыть страницу с формой авторизации")


def open_menu_desserts_section(browser):
    move_to_element(browser, (By.XPATH, "(//ul[contains(@class, 'menu intershop6')]/li)[2]"),
                    "Навести курсор на вкладку «Меню»")
    click_element(browser, (By.XPATH, "//a[contains(text(), 'Десерты')]"), "Нажать на ссылку раздела «Десерты»")


def open_loyalty_program_page(browser):
    click_element(browser, (By.XPATH, "//a[contains(text(), 'Бонусная программа')]"),
                  "Открыть страницу бонусной программы")
