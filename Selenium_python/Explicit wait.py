import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(3.5)
driver.get('https://www.flipkart.com/')
element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "myDynamicElement")))