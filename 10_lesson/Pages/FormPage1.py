from selenium.webdriver.common.by import By
import allure


class FormPage:

    def __init__(self, driver):
        """
            Инициализирует страницу с переданным драйвером.
        """
        self._driver = driver

    @allure.step("Заполнение полей персональными данными")
    def form(self):
        """
            Заполняет форму персональными данными
        """
        self._driver.find_element(By.ID, "first-name").send_keys("Гуманитарий")
        self._driver.find_element(By.ID, "last-name").send_keys("Техникумов")
        self._driver.find_element(By.ID, "postal-code").send_keys("160000")
        self._driver.find_element(By.ID, "continue").click()

    @allure.step("Получение информации о корзине")
    def total(self) -> str:
        """
            Возвращает информацию о сумме в корзине.
            :return: Текст, содержащий итоговую сумму
        """
        return self._driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
