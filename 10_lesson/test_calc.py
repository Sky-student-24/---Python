from selenium import webdriver
from Pages.CalculatorPage1 import CalculatorPage
import allure


@allure.title("Калькулятор")
@allure.feature("Google Chrome")
@allure.severity("normal")
@allure.description("Проверка корректного ожидания результата при вычмслениях")
def test_calculator():
    driver = webdriver.Chrome()

    calc_page = CalculatorPage(driver)
    with allure.step("Поиск числа 45"):
        calc_page.search("45")
    with allure.step("Нажатие кнопок"):
        calc_page.push_numbers()

    result = calc_page.results()
    with allure.step("Проверка результата"):
        assert result == "15"

    driver.quit()
