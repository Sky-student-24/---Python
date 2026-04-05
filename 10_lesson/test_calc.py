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
    calc_page.search("45")
    calc_page.push_numbers()

    result = calc_page.results()
    assert result == "15"

    driver.quit()
