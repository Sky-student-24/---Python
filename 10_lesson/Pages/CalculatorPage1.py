from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalculatorPage:

    def __init__(self, driver):
        """
            Инициализирует страницу с переданным драйвером.
        """
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.maximize_window()

    @allure.step("Ввод времени ожидания результата")
    def search(self, term: int):
        """
            Очищает поле ожидания результата и вводит заданное время
        """
        self._driver.find_element(By.ID, "delay").clear()
        self._driver.find_element(By.ID, "delay").send_keys(term)

    @allure.step("Ввод чисел")
    def push_numbers(self):
        """
            Производит набор символов для формирования результата
        """
        self._driver.find_element(By.XPATH, "//span[text()='7']").click()
        self._driver.find_element(By.XPATH, "//span[text()='+']").click()
        self._driver.find_element(By.XPATH, "//span[text()='8']").click()
        self._driver.find_element(By.XPATH, "//span[text()='=']").click()

    @allure.step("Проверка результата")
    def results(self) -> int:
        """
            Возвращает результат расчетов.
            :return: Число, получившееся в результате расчетов
        """
        wait = WebDriverWait(self._driver, 50)
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15"))
        return self._driver.find_element(By.CSS_SELECTOR, "div.screen").text
