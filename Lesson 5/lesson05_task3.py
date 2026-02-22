from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

firefox_options = Options()
service = Service()

driver = webdriver.Firefox(service=service, options=firefox_options)
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/inputs")

search_input = driver.find_element(By.CSS_SELECTOR, "input")
search_input.send_keys("Sky")
sleep(1)
search_input.clear()
sleep(1)
search_input.send_keys("Pro")
sleep(1)

driver.quit()
