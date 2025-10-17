from src.utils.web_helpers.common_imports import allure, WebDriverWait, EC, logging


logger = logging.getLogger("request")


def assert_element_visible(browser, locator, description):
    logger.info(description)
    with allure.step(description):
        el = WebDriverWait(browser, 30).until(
            EC.visibility_of_element_located(locator)
        )
        assert el.is_displayed()


def assert_text_in_element(browser, locator, text, description):
    logger.info(description)
    with allure.step(description):
        el = WebDriverWait(browser, 30).until(
            EC.visibility_of_element_located(locator)
        )
        actual_text = el.text.strip().replace("\xa0", " ")
        expected_text = text.strip().replace("\xa0", " ")

        assert expected_text.lower() in actual_text.lower()


def assert_attribute(element, attribute_name, expected_value: str, description):
    logger.info(description)
    with allure.step(description):
        actual_value = element.get_attribute(attribute_name)
        assert actual_value == expected_value


def assert_page_title(browser, expected_title: str, description):
    logger.info(description)
    with allure.step(description):
        actual_title = browser.title
        assert actual_title == expected_title
