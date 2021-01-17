import time,os
# модуль time для задержек, можно потом удалить их

''' для каждой страницы описыаем элементы, используя локаторы из файла locators '''

#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os
# модуль os чтобы использовать метод getenv чтобы получить доступ к переменным среды.
from pages.base_page import WebPage
from pages.webelements import WebElement
from pages.webelements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://tmall.ru/'

        super().__init__(web_driver, url)

    # Main search field
    search = WebElement(id='search-key')

    # Search button
    search_run_button = WebElement(xpath='//input[@type="submit"]')

    # Titles of the products in search results
    products_titles = ManyWebElements(xpath='//*[@id="hs-list-items"]//a[contains(@class, "product")]')

    # Button to sort products by price
    sort_products_by_price = WebElement(css_selector='a[data-filter-type="price"]')

    # Prices of the products in search results
    products_prices = ManyWebElements(xpath='//div[@class="price price-m"]//span[@itemprop="price"]')






