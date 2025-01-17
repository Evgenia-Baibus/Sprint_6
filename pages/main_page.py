from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    questions_section = [By.XPATH, "//div[text() = 'Вопросы о важном']"]

    payment_question_btn = [By.ID, 'accordion__heading-0']
    answer_payment_field = [By.ID, 'accordion__panel-0']

    scooters_number_question_btn = [By.ID, 'accordion__heading-1']
    answer_scooters_number_field = [By.ID, 'accordion__panel-1']

    rental_time_question_btn = [By.ID, 'accordion__heading-2']
    answer_rental_time_field = [By.ID, 'accordion__panel-2']

    order_today_question_btn = [By.ID, 'accordion__heading-3']
    answer_order_today_field = [By.ID, 'accordion__panel-3']

    order_extension_question_btn = [By.ID, 'accordion__heading-4']
    answer_order_extension_field = [By.ID, 'accordion__panel-4']

    scooter_charging_question_btn = [By.ID, 'accordion__heading-5']
    answer_scooter_charging_field = [By.ID, 'accordion__panel-5']

    cancel_order_question_btn = [By.ID, 'accordion__heading-6']
    answer_cancel_order_field = [By.ID, 'accordion__panel-6']

    delivery_area_question_btn = [By.ID, 'accordion__heading-7']
    answer_delivery_area_field = [By.ID, 'accordion__panel-7']

    header_order_btn = [By.CLASS_NAME, 'Button_Button__ra12g']
    bottom_order_btn = [By.CLASS_NAME, 'Button_Middle__1CSJM']

    close_cookies_btn = [By.ID, 'rcc-confirm-button']

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.questions_section))

    def scroll_to_questions_section(self):
        element = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.questions_section))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_question_answer(self, question_locator, answer_locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(question_locator)).click()
        answer = self.driver.find_element(*answer_locator).text
        return answer


    def scroll_to_bottom_order_btn(self):
        element = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.bottom_order_btn))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_bottom_order_btn(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.bottom_order_btn)).click()

    def click_close_cookies_btn(self):
        self.driver.find_element(*self.close_cookies_btn).click()





