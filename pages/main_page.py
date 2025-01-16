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

    def click_payment_question_btn(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.payment_question_btn))
        self.driver.find_element(*self.payment_question_btn).click()

    def check_answer_payment(self):
        actually_answer = self.driver.find_element(*self.answer_payment_field).text
        expected_answer = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
        assert actually_answer == expected_answer

    def click_scooters_number_btn(self):
        self.driver.find_element(*self.scooters_number_question_btn).click()

    def check_answer_scooters_number(self):
        actually_answer = self.driver.find_element(*self.answer_scooters_number_field).text
        expected_answer = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
        assert actually_answer == expected_answer

    def click_rental_time_btn(self):
        self.driver.find_element(*self.rental_time_question_btn).click()

    def check_answer_rental_time(self):
        actually_answer = self.driver.find_element(*self.answer_rental_time_field).text
        expected_answer = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
        assert actually_answer == expected_answer

    def click_order_today_btn(self):
        self.driver.find_element(*self.order_today_question_btn).click()

    def check_answer_order_today(self):
        actually_answer = self.driver.find_element(*self.answer_order_today_field).text
        expected_answer = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
        assert actually_answer == expected_answer

    def click_order_extension_btn(self):
        self.driver.find_element(*self.order_extension_question_btn).click()

    def check_answer_order_extension(self):
        actually_answer = self.driver.find_element(*self.answer_order_extension_field).text
        expected_answer = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
        assert actually_answer == expected_answer

    def click_scooter_charging_btn(self):
        self.driver.find_element(*self.scooter_charging_question_btn).click()

    def check_answer_scooter_charging(self):
        actually_answer = self.driver.find_element(*self.answer_scooter_charging_field).text
        expected_answer = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
        assert actually_answer == expected_answer

    def click_cancel_order_btn(self):
        self.driver.find_element(*self.cancel_order_question_btn).click()

    def check_answer_cancel_order(self):
        actually_answer = self.driver.find_element(*self.answer_cancel_order_field).text
        expected_answer = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
        assert actually_answer == expected_answer

    def click_delivery_area_btn(self):
        self.driver.find_element(*self.delivery_area_question_btn).click()

    def check_answer_delivery_area(self):
        actually_answer = self.driver.find_element(*self.answer_delivery_area_field).text
        expected_answer = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
        assert actually_answer == expected_answer

    def click_header_order_btn(self):

        self.driver.find_element(*self.header_order_btn).click()

    def scroll_to_bottom_order_btn(self):
        element = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.bottom_order_btn))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_bottom_order_btn(self):
        self.driver.find_element(*self.bottom_order_btn).click()

    def click_close_cookies_btn(self):
        self.driver.find_element(*self.close_cookies_btn).click()





