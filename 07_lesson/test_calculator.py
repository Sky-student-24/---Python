from selenium import webdriver
from Pages.CalculatorPage import CalculatorPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator():
    driver = webdriver.Chrome()

    calc_page = CalculatorPage(driver)
    calc_page.search("45")
    calc_page.push_numbers()

    wait = WebDriverWait(driver, 45)
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15"))

    result = calc_page.results()
    assert result == "15"

    driver.quit
