import time
import allure
from data import OrderDetails
from pages.main_page import MainPage
from pages.order_page import OrderPage
from urls import Urls


class TestOrderPage:

    @allure.title('Проверка заказа самоката через кнопку "Заказать" вверху страницы')
    @allure.description('Нажимаем на кнопку "Заказать" вверху страницы, заполняем форму заказа и проверяем, что появилось всплывающее окно с сообщением об успешном создании заказа.')
    def test_order_scooters_by_order_button_in_header(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.click_close_cookies_btn()
        main_page.click_header_order_btn()

        order_page.wait_for_load_order_page()
        order_page.order_scooter(OrderDetails.details_1())

    @allure.title('Проверка заказа самоката через кнопку "Заказать" вверху страницы')
    @allure.description('Проскролливаем до кнопки "Заказать" внизу страницы и нажимаем на нее, заполняем форму заказа и проверяем, что появилось всплывающее окно с сообщением об успешном создании заказа.')
    def test_order_scooters_by_order_button_in_bottom(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.click_close_cookies_btn()
        main_page.scroll_to_bottom_order_btn()
        main_page.click_bottom_order_btn()

        order_page.wait_for_load_order_page()
        order_page.order_scooter(OrderDetails.details_2())

    @allure.title('Проверка перехода на главную страницу через клик на логотип Самоката')
    @allure.description('Принимаем куки и кликаем на логотип самоката')
    def test_transition_to_main_page_via_scooter_logo(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.click_close_cookies_btn()
        main_page.click_header_order_btn()

        order_page.click_scooter_logo()
        assert driver.current_url == Urls.MAIN_PAGE

    @allure.title('Проверка редиректа на главную страницу Дзкна через клик на логотип Яндекса')
    @allure.description('Кликаем на логотип Яндекса')
    def test_transition_to_dzen_page_via_yandex_logo(self, driver):
        order_page = OrderPage(driver)

        order_page.click_yandex_logo()
        order_page.go_to_new_tab()
        time.sleep(5)
        current_url = driver.current_url
        assert current_url == Urls.DZEN

