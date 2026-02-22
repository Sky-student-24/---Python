from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome_options = Options()
service = Service()

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

driver.get("http://uitestingplayground.com/classattr")

wait = WebDriverWait(driver, 10)
button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "btn-primary")))
button.click()

# Закрытие окна с подтверждением
alert = driver.switch_to.alert
alert.accept()

sleep(1)

driver.quit()
