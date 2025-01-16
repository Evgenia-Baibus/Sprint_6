from selenium import webdriver
from pages.main_page import HomePage
from pages.order_page import OrderPage


class TestOrderPage:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    def test_order_scooters_by_order_button_in_header(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        home_page = HomePage(self.driver)
        order_page = OrderPage(self.driver)

        home_page.wait_for_load_home_page()
        home_page.click_close_cookies_btn()
        home_page.click_header_order_btn()

        order_page.wait_for_load_order_page()
        order_page.order_scooter()

    def test_order_scooters_by_order_button_in_bottom(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        home_page = HomePage(self.driver)
        order_page = OrderPage(self.driver)

        home_page.wait_for_load_home_page()
        home_page.click_close_cookies_btn()
        home_page.scroll_to_bottom_order_btn()
        home_page.click_bottom_order_btn()

        order_page.wait_for_load_order_page()
        order_page.order_scooter()



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

class User:
    pass