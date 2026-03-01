from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
service = Service()

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
waiter = WebDriverWait(driver, 40)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

waiter.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#landscape")))

search_src = driver.find_element(By.CSS_SELECTOR, "#award").get_attribute("src")

print(search_src)

driver.quit()
