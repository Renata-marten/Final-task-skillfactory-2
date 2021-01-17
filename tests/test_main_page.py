from selenium import webdriver
import config
import time
# time для задержек времени, можно потом убрать их все
import pytest
from pages.main_page import MainPage
# импортируем класс страницы

''' для каждой страницы пишем тесты, используя элементы предварительно описанные в файле страницы '''

def test_check_main_search(web_browser):
    """ Make sure main search works fine. """

    page = MainPage(web_browser)

    page.search = 'iPhone 12'
    page.search_run_button.click()

    # Verify that user can see the list of products:
    assert page.products_titles.count() == 48