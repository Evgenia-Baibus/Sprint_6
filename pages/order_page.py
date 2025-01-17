from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class OrderPage:
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



    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_order_page(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.next_btn))

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
        self.driver.find_element(*self.name_input).send_keys(name)

    def set_last_name(self, last_name):
        self.driver.find_element(*self.last_name_input).send_keys(last_name)

    def set_address(self, address):
        self.driver.find_element(*self.address_input).send_keys(address)

    @staticmethod
    def metro_selection_locator(station):
        return By.XPATH, f"//div[text() = '{station}']"

    def select_metro_station(self, station):
        self.driver.find_element(*self.metro_station_input).click()
        self.driver.find_element(*self.metro_station_input).send_keys(station)
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.metro_selection_locator(station))).click()

    def set_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_input).send_keys(phone_number)

    def click_next_btn(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.next_btn)).click()

    @staticmethod
    def delivery_data_locator(day):
        if day < 10:
            day = f"00{day}"
        else:
            day = f"0{day}"
        return By.CLASS_NAME, f"react-datepicker__day--{day}"


    def select_delivery_data(self, day):
        self.driver.find_element(*self.delivery_data_input).click()
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.delivery_data_locator(day))).click()

    @staticmethod
    def rental_period_locator(period):
        return By.XPATH, f"//div[text() = '{period}']"

    def select_rental_period(self,period):
        self.driver.find_element(*self.rental_period_list).click()
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.rental_period_locator(period))).click()

    @staticmethod
    def scooter_color_locator(color):
        return By.XPATH, f"//input[@id = '{color}']"

    def click_scooter_color(self, color):
        self.driver.find_element(*self.scooter_color_locator(color)).click()

    def set_comment(self, comment):
        self.driver.find_element(*self.comment_input).send_keys(comment)

    def click_order_btn(self):
        button = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.order_btn))
        button.click()


    def click_yes_order_pop_up_btn(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.yes_order_pop_up_btn)).click()


    def check_success_order_pop_up(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.view_status_btn))

    def click_view_status_btn(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.view_status_btn)).click()

    def click_scooter_logo(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.scooter_logo)).click()

    def click_yandex_logo(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.yandex_logo)).click()

    def go_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
