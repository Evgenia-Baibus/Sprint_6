from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class OrderPage(BasePage):
    name_input = [By.XPATH, './/input[@placeholder = "* Имя"]']
    last_name_input = [By.XPATH, './/input[@placeholder = "* Фамилия"]']
    address_input =  [By.XPATH, './/input[@placeholder = "* Адрес: куда привезти заказ"]']
    metro_station_input = [By.XPATH, './/input[@placeholder = "* Станция метро"]']
    phone_input = [By.XPATH, './/input[@placeholder = "* Телефон: на него позвонит курьер"]']
    next_btn = [By.XPATH, './/button[text() = "Далее"]']

    delivery_data_input = [By.XPATH, './/input[@placeholder= "* Когда привезти самокат"]']
    rental_period_list = [By.CLASS_NAME, 'Dropdown-placeholder']
    comment_input = [By.XPATH, './/input[@placeholder = "Комментарий для курьера"]']
    order_btn = [By.XPATH, '(.//button[text() = "Заказать"])[2]']

    yes_order_pop_up_btn = [By.XPATH, './/button[text() = "Да"]']

    view_status_btn = [By.XPATH, './/button[text()= "Посмотреть статус"]']

    scooter_logo = [By.XPATH, './/img[@alt = "Scooter"]']
    yandex_logo = [By.XPATH, './/img[@alt = "Yandex"]']

    def wait_for_load_order_page(self):
        self.wait_for_element(self.next_btn)

    def order_scooter(self, order_details):
        self.set_name(order_details.name)
        self.set_last_name(order_details.last_name)
        self.set_address(order_details.address)
        self.select_metro_station(order_details.station)
        self.set_phone_number(order_details.phone_number)
        self.click_next_btn()

        self.select_delivery_data(order_details.day)
        self.select_rental_period(order_details.period)
        self.click_scooter_color(order_details.color)
        self.set_comment(order_details.comment)
        self.click_order_btn()
        self.click_yes_order_pop_up_btn()
        self.check_success_order_pop_up()



    def set_name(self, name):
        self.send_keys_to_input(self.name_input, name)

    def set_last_name(self, last_name):
       self.send_keys_to_input(self.last_name_input, last_name)

    def set_address(self, address):
        self.send_keys_to_input(self.address_input, address)

    @staticmethod
    def metro_selection_locator(station):
        return By.XPATH, f"//div[text() = '{station}']"

    def select_metro_station(self, station):
        self.click_element(self.metro_station_input)
        self.send_keys_to_input(self.metro_station_input, station)
        self.click_element(self.metro_selection_locator(station))

    def set_phone_number(self, phone_number):
        self.send_keys_to_input(self.phone_input, phone_number)

    def click_next_btn(self):
        self.click_element(self.next_btn)

    @staticmethod
    def delivery_data_locator(day):
        if day < 10:
            day = f"00{day}"
        else:
            day = f"0{day}"
        return By.CLASS_NAME, f"react-datepicker__day--{day}"


    def select_delivery_data(self, day):
        self.click_element(self.delivery_data_input)
        self.click_element(self.delivery_data_locator(day))

    @staticmethod
    def rental_period_locator(period):
        return By.XPATH, f"//div[text() = '{period}']"

    def select_rental_period(self,period):
        self.click_element(self.rental_period_list)
        self.click_element(self.rental_period_locator(period))

    @staticmethod
    def scooter_color_locator(color):
        return By.XPATH, f"//input[@id = '{color}']"

    def click_scooter_color(self, color):
        self.click_element(self.scooter_color_locator(color))

    def set_comment(self, comment):
        self.send_keys_to_input(self.comment_input, comment)

    def click_order_btn(self):
        self.click_element(self.order_btn)

    def click_yes_order_pop_up_btn(self):
        self.click_element(self.yes_order_pop_up_btn)

    def check_success_order_pop_up(self):
        self.wait_for_element(self.view_status_btn)

    def click_view_status_btn(self):
        self.click_element(self.view_status_btn)

    def click_scooter_logo(self):
        self.click_element(self.scooter_logo)

    def click_yandex_logo(self):
        self.click_element(self.yandex_logo)

    def go_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
