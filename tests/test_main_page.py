from selenium import webdriver

from data import QuestionAnswers
from locators import QuestionsLocators, AnswersLocators
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
        zip(QuestionsLocators.locators, AnswersLocators.locators, QuestionAnswers.answers)
    )
    def test_question_answer(self, question_locator, answer_locator, expected_answer):
        self.home_page.wait_for_load_home_page()
        self.home_page.scroll_to_questions_section()
        answer = self.home_page.get_question_answer(question_locator, answer_locator)
        assert answer == expected_answer

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

