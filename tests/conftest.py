import pytest
from selenium import webdriver

from urls import Urls


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.MAIN_PAGE)
    yield driver
    driver.quit()