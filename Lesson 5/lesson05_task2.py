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

driver.get("http://uitestingplayground.com/dynamicid")

wait = WebDriverWait(driver, 10)
button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "btn-primary")))
button.click()

sleep(1)

driver.quit()
