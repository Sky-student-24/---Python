from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_fill_form():
    driver = webdriver.Edge()
    driver.maximize_window()

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

# Заполняем форму
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    driver.find_element(By.CSS_SELECTOR, "button.btn").click()

# Ждем загрузки результатов
    wait = WebDriverWait(driver, 5)

# Проверяем, что поле Zip code подсвечено красным
    zip_code_element = wait.until(
        EC.presence_of_element_located((By.ID, "zip-code"))
    )
    assert "alert-danger" in zip_code_element.get_attribute("class"), "Zip code не подсвечен красным"

# Правильные ID полей для проверки (согласно HTML страницы)
    fields_to_check = [
        "first-name",
        "last-name",
        "address",
        "city",
        "country",
        "e-mail",
        "phone",
        "job-position",
        "company"
    ]

# Проверяем остальные поля (должны быть зелеными)
    for field_id in fields_to_check:
        # Добавляем ожидание для каждого поля
        element = wait.until(
            EC.presence_of_element_located((By.ID, field_id))
        )
        class_name = element.get_attribute("class")
        assert "alert-success" in class_name, \
            f"Поле '{field_id}' не подсвечено зеленым. Найден класс: {class_name}"

    driver.quit()
