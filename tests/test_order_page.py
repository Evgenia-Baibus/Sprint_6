import time

from selenium import webdriver

from data import OrderDetails
from pages.main_page import MainPage
from pages.order_page import OrderPage
from urls import Urls


class TestOrderPage:


    def test_order_scooters_by_order_button_in_header(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.click_close_cookies_btn()
        main_page.click_header_order_btn()

        order_page.wait_for_load_order_page()
        order_page.order_scooter(OrderDetails.details_1())

    def test_order_scooters_by_order_button_in_bottom(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.click_close_cookies_btn()
        main_page.scroll_to_bottom_order_btn()
        main_page.click_bottom_order_btn()

        order_page.wait_for_load_order_page()
        order_page.order_scooter(OrderDetails.details_2())

    def test_transition_to_main_page_via_scooter_logo(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.click_close_cookies_btn()
        main_page.click_header_order_btn()

        order_page.click_scooter_logo()
        assert driver.current_url == Urls.MAIN_PAGE

    def test_transition_to_dzen_page_via_yandex_logo(self, driver):
        order_page = OrderPage(driver)

        order_page.click_yandex_logo()
        order_page.go_to_new_tab()
        time.sleep(5)
        current_url = driver.current_url
        assert current_url == Urls.DZEN

