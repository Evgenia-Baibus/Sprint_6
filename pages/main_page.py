from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    questions_section = [By.XPATH, "//div[text() = 'Вопросы о важном']"]

    header_order_btn = [By.CLASS_NAME, 'Button_Button__ra12g']
    bottom_order_btn = [By.CLASS_NAME, 'Button_Middle__1CSJM']

    close_cookies_btn = [By.ID, 'rcc-confirm-button']


    def wait_for_load_main_page(self):
        self.wait_for_element(self.questions_section)

    def scroll_to_questions_section(self):
        self.scroll_to_element(self.questions_section)

    def get_question_answer(self, question_locator, answer_locator):
        self.click_element(question_locator)
        answer = self.driver.find_element(*answer_locator).text
        return answer

    def scroll_to_bottom_order_btn(self):
        self.scroll_to_element(self.bottom_order_btn)

    def click_bottom_order_btn(self):
        self.click_element(self.bottom_order_btn)

    def click_close_cookies_btn(self):
        self.click_element(self.close_cookies_btn)

    def click_header_order_btn(self):
        self.click_element(self.header_order_btn)