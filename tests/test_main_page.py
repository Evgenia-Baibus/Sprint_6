from selenium import webdriver
from pages.main_page import HomePage

class TestDropdownListQuestions:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get('https://qa-scooter.praktikum-services.ru/')
        cls.home_page = HomePage(cls.driver)

    def test_dropdown_question_payment_answer(self):
        self.home_page.wait_for_load_home_page()
        self.home_page.scroll_to_questions_section()
        self.home_page.click_payment_question_btn()
        self.home_page.check_answer_payment()

    def test_dropdown_question_scooters_number_answer(self):
        self.home_page.wait_for_load_home_page()
        self.home_page.scroll_to_questions_section()
        self.home_page.click_scooters_number_btn()
        self.home_page.check_answer_scooters_number()

    def test_dropdown_question_rental_time_answer(self):
        self.home_page.wait_for_load_home_page()
        self.home_page.scroll_to_questions_section()
        self.home_page.click_rental_time_btn()
        self.home_page.check_answer_rental_time()

    def test_dropdown_question_order_today_answer(self):
        self.home_page.wait_for_load_home_page()
        self.home_page.scroll_to_questions_section()
        self.home_page.click_order_today_btn()
        self.home_page.check_answer_order_today()

    def test_dropdown_question_order_extension_answer(self):
        self.home_page.wait_for_load_home_page()
        self.home_page.scroll_to_questions_section()
        self.home_page.click_order_extension_btn()
        self.home_page.check_answer_order_extension()

    def test_dropdown_question_scooter_charging(self):
        self.home_page.wait_for_load_home_page()
        self.home_page.scroll_to_questions_section()
        self.home_page.click_scooter_charging_btn()
        self.home_page.check_answer_scooter_charging()

    def test_dropdown_question_cancel_order(self):
        self.home_page.wait_for_load_home_page()
        self.home_page.click_cancel_order_btn()
        self.home_page.check_answer_cancel_order()

    def test_dropdown_question_delivery_area(self):
        self.home_page.wait_for_load_home_page()
        self.home_page.scroll_to_questions_section()
        self.home_page.click_delivery_area_btn()
        self.home_page.check_answer_delivery_area()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()