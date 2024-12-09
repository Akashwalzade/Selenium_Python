from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

import time
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options= options)
driver.maximize_window()
# driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.get('https://www.flipkart.com/')

# blinking_link = driver.find_element(By.CLASS_NAME, "blinkingText")
# print(blinking_link.get_attribute("href"))

# for button //button[text()='save']

deal_banner = driver.find_elements(By.XPATH, '//div[@data-clone="false"]//a')
print(f"total no of deals: {len(deal_banner)}")

for deal_banner in deal_banner:
    print(deal_banner.get_attribute("href"))