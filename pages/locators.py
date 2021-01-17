# здесь сначала пишем локаторы элементов страниц, которые собираемся использовать в проверках

from selenium.webdriver.common.by import By
# импортируем класс, содержащий определения разных типов поиска

class Locators:
    LOGO_GIF = (By.CLASS_NAME, "site-gif")
    LOGO_ALI = (By.CLASS_NAME, "logo-link")
    SEARCH_FIELD = (By.ID, "search-key")
    SEARCH_BUTTON = (By.CLASS_NAME, "search-button")
    PRODUCT_ITEMS = (By.XPATH, '//*[@id="hs-list-items"]//a[contains(@class, "product")]')

