from selenium.webdriver.common.by import By
import allure


class BasketPage:

    def __init__(self, driver):
        self._driver = driver

    @allure.step("Перейти в корзину")
    def get(self):
        self._driver.get("https://www.saucedemo.com/cart.html")

    @allure.step("Проверка выбранных товаров")
    def check(self):
        self._driver.find_element(By.ID, "checkout").click()
