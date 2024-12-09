from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


options = Options()
options.add_experimental_option("detach",True)

driver =webdriver.Chrome(options = options)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.XPATH, '*//*[@id="autocomplete"]').send_keys("india")

# static_dropdown = driver.find_element(By.ID, "dropdown-class-example")
# select = Select(static_dropdown)
# select.select_by_index(2)
# time.sleep(2)
# select.select_by_value("option1")
# time.sleep(1)
# select.select_by_visible_text("Option3")

value3 = driver.find_element(By.XPATH, "//option[@value=\"option3\"]")
time.sleep(2)
value3.click()

# Norte for select there should be select tag compulsory for the elements