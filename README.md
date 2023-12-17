# Проект автоматизации тестирования с использованием Selenium и Pytest
Проект создан с целью демонстрации навыков в области автоматизации тестирования на языке программирования Python. 
В проекте реализованы автоматизированные тесты для трех сценариев, используя Selenium WebDriver и фреймворк Pytest. 
Один из сценариев реализует возможность скачивания файлов с проверкой успешности загрузки.

В качестве источников используются сайты https://sbis.ru/ и https://tensor.ru/.

## Настройки
Основные настройки проекта приведены в файле `config.py`

## Требования
* Python 3
* Установленные зависимости из `requirements.txt`
* Браузер Chrome 
* Просмотр результатов тестов в виде отчета требует наличие установленной зависимости Allure

## Использование
1. Запуск тестов
```shell
  pytest -sv --alluredir=allure-results
```
2. Просмотр результатов тестов
```shell
  allure serve allure-results
```