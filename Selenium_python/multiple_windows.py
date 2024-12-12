import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = options)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

print(driver.window_handles)
print("**************")
driver.find_element("xpath", '//*[text()="Open Window"]').click()
time.sleep(2)

print(driver.window_handles)
print("**************")
driver.find_element("xpath", '//*[text()="Open Tab"]').click()
time.sleep(2)
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[1])
driver.find_element("xpath", '//*[contains(@href, "/blog")][1]').click()

