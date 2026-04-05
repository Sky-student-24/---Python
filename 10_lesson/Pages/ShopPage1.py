from selenium.webdriver.common.by import By
import allure


class ShopPage:

    def __init__(self, driver):
        """
            Инициализирует страницу с переданным драйвером.
        """
        self._driver = driver

    @allure.step("Добавление товаров в корзину")
    def shop(self):
        """
            Отправляет выбранные товары в корзину
        """
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
