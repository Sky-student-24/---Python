from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.maximize_window()

    def search(self, term):
        self._driver.find_element(By.ID, "delay").clear()
        self._driver.find_element(By.ID, "delay").send_keys(term)

    def push_numbers(self):
        self._driver.find_element(By.XPATH, "//span[text()='7']").click()
        self._driver.find_element(By.XPATH, "//span[text()='+']").click()
        self._driver.find_element(By.XPATH, "//span[text()='8']").click()
        self._driver.find_element(By.XPATH, "//span[text()='=']").click()

        wait = WebDriverWait(self._driver, 45)
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15"))

    def results(self):
        return self._driver.find_element(By.CSS_SELECTOR, "div.screen").text
