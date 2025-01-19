# Автотесты для сервиса [Яндекс.Самокат](https://qa-scooter.praktikum-services.ru/)

Сервис [Яндекс.Самокат](https://qa-scooter.praktikum-services.ru) - это сайт для аренды самоката.

## Структура проекта 

* [tests](tests) - директория с тестами
* [tests](tests/test_main_page.py)- файл с проверками главной страницы
* [tests](tests/test_order_page.py) - файл с проверками страницы заказа
* [pages](pages) - директория с Pages Objects
* [pages/base_page](pages/base_page) - файл с базовыми функциями, характерными для всех страниц
* [pages/main_pages](pages/main_page) - файл с Pages Objects главной страницы
* [pages/order_pages](pages/order_page) - файл с Pages Objects страницы заказа
* [conftest.py](conftest.py) - файл с фикстурами
* [data.py](data.py) - файл с данными заказа самоката и ответами на вопросы на главной странице
* [locators.py](locators.py) - файл с локаторами элементов
* [urls.py](urls.py) - файл с урлами страниц
* [allure_results](allure_results) - каталог с отчетом тестирования

## Запуск тестов

Для запуска тестов выполнить:
```bash
pytest
```