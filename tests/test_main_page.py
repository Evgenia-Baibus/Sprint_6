from data import QuestionAnswers
from locators import QuestionsLocators, AnswersLocators
from pages.main_page import MainPage
import pytest
import allure


class TestMainPage:

    @allure.title('Проверка выпадающего списка в разделе "Вопросы о важном"')
    @allure.description('На странице нажимаем на вопрос и проверяем, что открывается соответствующий ответ')
    @pytest.mark.parametrize(
        'question_locator, answer_locator, expected_answer',
        zip(QuestionsLocators.locators, AnswersLocators.locators, QuestionAnswers.answers)
    )
    def test_question_answer(self, driver, question_locator, answer_locator, expected_answer):
        home_page = MainPage(driver)
        home_page.scroll_to_questions_section()
        answer = home_page.get_question_answer(question_locator, answer_locator)
        assert answer == expected_answer

