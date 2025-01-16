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
    data_picker = [By.XPATH, './/div[@aria-label = "Choose понедельник, 13-е января 2025 г."]']
    rental_period_list = [By.CLASS_NAME, 'Dropdown-placeholder']
    selected_rental_period = [By.XPATH, './/div[text()= "сутки"]']
    scooter_color_checkbook = [By.XPATH, './/input[@id= "black"]']
    comment_input = [By.XPATH, './/input[@placeholder = "Комментарий для курьера"]']
    order_btn = [By.XPATH, '(.//button[text() = "Заказать"])[2]']

    yes_order_pop_up_btn = [By.XPATH, './/button[text() = "Да"]']

    success_order_pop_up = [By.XPATH, './/div[text()= "Заказ оформлен"]']



    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_order_page(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.next_btn))

    def order_scooter(self):
        self.set_name('Людмила')
        self.set_last_name('Гребенщикова')
        self.set_address('ул. Пушкина, д. Колотушкина')
        self.select_metro_station('Парк культуры')
        self.set_phone_number('+385445647382')
        self.click_next_btn()

        self.select_delivery_data()
        self.select_rental_period()
        self.click_scooter_color()
        self.set_comment('Hello')
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

    def select_delivery_data(self):
        self.driver.find_element(*self.delivery_data_input).click()
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.data_picker)).click()

    def select_rental_period(self):
        self.driver.find_element(*self.rental_period_list).click()
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.selected_rental_period)).click()

    def click_scooter_color(self):
        self.driver.find_element(*self.scooter_color_checkbook).click()

    def set_comment(self, comment):
        self.driver.find_element(*self.comment_input).send_keys(comment)

    def click_order_btn(self):
        button = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.order_btn))
        button.click()


    def click_yes_order_pop_up_btn(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.yes_order_pop_up_btn)).click()


    def check_success_order_pop_up(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.success_order_pop_up))
