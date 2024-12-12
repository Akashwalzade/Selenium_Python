from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = options)
driver.maximize_window()
driver.get('https://www.flipkart.com/')

hover_element = driver.find_element("xpath", '(//*[text()="Login"])[1]')

action = ActionChains(driver)
action.move_to_element(hover_element).perform()
my_profile = driver.find_element("xpath", '//*[text()="My Profile"]')
action.move_to_element(my_profile).click().perform()

# action.move_to_element(my_profile).double_click()
