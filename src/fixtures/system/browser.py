import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def browser(pytestconfig):
    options = Options()
    options.page_load_strategy = "normal"
    browser_name = pytestconfig.getini("browser_name")
    logging.info(f"Prepare {browser_name} browser...")
    if pytestconfig.getini("headless") == "True" and browser_name == "chrome":
        options.add_argument("--headless")

    driver = webdriver.Remote(
        command_executor=pytestconfig.getini("selenium_url"),
        options=options
    )
    logging.info(f"Browser {browser_name} has been started.")
    yield driver
    driver.quit()


@pytest.fixture()
def new_fixure():
    pass
