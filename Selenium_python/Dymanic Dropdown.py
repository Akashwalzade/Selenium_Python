import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get('https://www.flipkart.com/')
search_box = driver.find_element(By.XPATH, "//input[@class = 'Pke_EE']")
search_box.send_keys("one plus headphones")
time.sleep(2)
first_option = driver.find_element(By.XPATH, '(//*[@class="_2rslOn header-form-search OpXDaO"]//a)[1]')
# first_option = driver.find_element("xpath" '(//*[@class="_2rslOn header-form-search OpXDaO"]//a)[1]')

# print(f"link present in first option:{first_option.get_attribute('href')}")
# print(f"text present in first option:{first_option.text}")
# first_option.click()
# print(driver.current_url)

dropdown = driver.find_elements(By.XPATH, '(//*[@class="_2rslOn header-form-search OpXDaO"]//a)')
for index,options in enumerate(dropdown):
    print(f"link present in {index+1} first option:{options.get_attribute('href')}")
    print(f"text present in {index+1} first option:{options.text}")

    if "headphones" in options.text:
        options.click()

        break

else:
    print("headphones not found")



