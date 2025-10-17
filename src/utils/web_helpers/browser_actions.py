from src.utils.web_helpers.common_imports import allure, WebDriverWait, EC, ActionChains, Keys, logging, By


logger = logging.getLogger("request")


def open_page(browser, url, description):
    logger.info(description)
    with allure.step(description):
        browser.get(url)
        WebDriverWait(browser, 30).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )


def click_element(browser, locator, description):
    logger.info(description)
    with allure.step(description):
        el = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable(locator)
        )
        el.click()


def input_text(browser, locator, text, description):
    logger.info(description)
    with allure.step(description):
        el = WebDriverWait(browser, 30).until(
            EC.visibility_of_element_located(locator)
        )
        el.clear()
        el.send_keys(text)


def press_enter(browser, locator, description="Нажать ENTER"):
    with allure.step(description):
        el = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable(locator)
        )
        el.send_keys(Keys.ENTER)


def move_to_element(browser, locator, description):
    logger.info(description)
    with allure.step(description):
        el = WebDriverWait(browser, 30).until(
            EC.visibility_of_element_located(locator)
        )
        ActionChains(browser).move_to_element(el).perform()


def move_slider(browser, locator, x_offset: int, description):
    with allure.step(description):
        slider = WebDriverWait(browser, 30).until(
            EC.visibility_of_element_located(locator)
        )
        ActionChains(browser).click_and_hold(slider).move_by_offset(x_offset, 0).release().perform()


def wait_for_element(browser, locator, description, timeout):
    logger.info(description)
    with allure.step(description):
        WebDriverWait(browser, timeout).until(
            EC.visibility_of_element_located(locator)
        )
