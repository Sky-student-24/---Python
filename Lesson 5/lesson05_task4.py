from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

firefox_options = Options()
service = Service()

driver = webdriver.Firefox(service=service, options=firefox_options)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/login")

search_name = driver.find_element(By.CSS_SELECTOR, "#username")
search_name.send_keys("tomsmith")

search_password = driver.find_element(By.CSS_SELECTOR, "#password")
search_password.send_keys("SuperSecretPassword!")

search_button_login = driver.find_element(By.CSS_SELECTOR, "button")
search_button_login.click()

success_message = driver.find_element(By.CSS_SELECTOR, "div.flash.success")
print(success_message.text)

sleep(1)

driver.quit()
