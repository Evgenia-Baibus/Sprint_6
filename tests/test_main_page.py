from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.main_page import HomePage
from urls import Urls
import pytest


class TestDropdownListQuestions:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get(Urls.MAIN_PAGE)
        cls.home_page = HomePage(cls.driver)

    @pytest.mark.parametrize(
        'question_locator, answer_locator, expected_answer',
        [
            [[By.ID, 'accordion__heading-0'], [By.ID, 'accordion__panel-0'], 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'],
            [[By.ID, 'accordion__heading-1'], [By.ID, 'accordion__panel-1'], 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'],
            [[By.ID, 'accordion__heading-2'], [By.ID, 'accordion__panel-2'], 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'],
            [[By.ID, 'accordion__heading-3'], [By.ID, 'accordion__panel-3'], 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'],
            [[By.ID, 'accordion__heading-4'], [By.ID, 'accordion__panel-4'], 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'],
            [[By.ID, 'accordion__heading-5'], [By.ID, 'accordion__panel-5'], 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'],
            [[By.ID, 'accordion__heading-6'], [By.ID, 'accordion__panel-6'], 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'],
            [[By.ID, 'accordion__heading-7'], [By.ID, 'accordion__panel-7'], 'Да, обязательно. Всем самокатов! И Москве, и Московской области.']
        ]
    )
    def test_question_answer(self, question_locator, answer_locator, expected_answer):
        self.home_page.wait_for_load_home_page()
        self.home_page.scroll_to_questions_section()
        answer = self.home_page.get_question_answer(question_locator, answer_locator)
        assert answer == expected_answer

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
