
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop_buy():
    driver = webdriver.Firefox()
    driver.maximize_window()

    driver.get("https://www.saucedemo.com/")

# Авторизация
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

# Заполнение корзины
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()

# Заполнение персональных данных
    driver.find_element(By.ID, "first-name").send_keys("Гуманитарий")
    driver.find_element(By.ID, "last-name").send_keys("Техникумов")
    driver.find_element(By.ID, "postal-code").send_keys("160000")

    driver.find_element(By.ID, "continue").click()

    wait = WebDriverWait(driver, 5)

    total = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.summary_total_label")))

    print(total)

    driver.quit()
