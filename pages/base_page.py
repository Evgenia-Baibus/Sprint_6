from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))

    def click_button(self, locator):
        self.wait_for_element(locator).click()

    def send_keys_to_input(self, locator, value):
        self.wait_for_element(locator).send_keys(value)

    def scroll_to_element(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
