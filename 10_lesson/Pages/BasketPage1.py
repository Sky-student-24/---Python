from selenium.webdriver.common.by import By
import allure


class BasketPage:

    def __init__(self, driver):
        """
            Инициализирует страницу с переданным драйвером.
        """
        self._driver = driver

    @allure.step("Перейти в корзину")
    def get(self):
        """
            Переходит на сайт корзины пользователя
        """
        self._driver.get("https://www.saucedemo.com/cart.html")

    @allure.step("Проверка выбранных товаров")
    def check(self):
        """
            Открывает подробную информацию о корзине пользователя
        """
        self._driver.find_element(By.ID, "checkout").click()
