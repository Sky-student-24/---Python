from selenium.webdriver.common.by import By


class FormPage:

    def __init__(self, driver):
        self._driver = driver

    def form(self):
        self._driver.find_element(By.ID, "first-name").send_keys("Гуманитарий")
        self._driver.find_element(By.ID, "last-name").send_keys("Техникумов")
        self._driver.find_element(By.ID, "postal-code").send_keys("160000")
        self._driver.find_element(By.ID, "continue").click()

    def total(self):
        return self._driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
