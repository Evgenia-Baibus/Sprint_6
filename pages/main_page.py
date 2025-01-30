import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage



class MainPage(BasePage):
    questions_section = [By.XPATH, "//div[text() = 'Вопросы о важном']"]

    header_order_btn = [By.CLASS_NAME, 'Button_Button__ra12g']
    bottom_order_btn = [By.CLASS_NAME, 'Button_Middle__1CSJM']

    close_cookies_btn = [By.ID, 'rcc-confirm-button']

    @allure.step('Проскроллить до раздела "Вопросы о важном"')
    def scroll_to_questions_section(self):
        self.scroll_to_element(self.questions_section)

    @allure.step('Кликнуть на вопрос и получить значение текста ответа"')
    def get_question_answer(self, question_locator, answer_locator):
        self.click_element(question_locator)
        answer = self.driver.find_element(*answer_locator).text
        return answer

    @allure.step('Проскроллить до кнопки заказа самоката')
    def scroll_to_bottom_order_btn(self):
        self.scroll_to_element(self.bottom_order_btn)

    @allure.step('Кликнуть на кнопку заказа самоката внизу страницы')
    def click_bottom_order_btn(self):
        self.click_element(self.bottom_order_btn)

    @allure.step('Принять куки')
    def click_close_cookies_btn(self):
        self.click_element(self.close_cookies_btn)

    @allure.step('Кликнуть на кнопку заказа самоката вверху страницы')
    def click_header_order_btn(self):
        self.click_element(self.header_order_btn)