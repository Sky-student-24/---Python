from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
service = Service()

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

driver.get("http://uitestingplayground.com/textinput")

search_input = driver.find_element(By.CSS_SELECTOR, "input")
search_input.send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, "button.btn-primary").click()

txt = driver.find_element(By.CSS_SELECTOR, "button.btn-primary").text

print(txt)

driver.quit()
