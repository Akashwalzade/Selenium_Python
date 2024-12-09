

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


options = Options()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options = options)
driver.maximize_window()
driver.get("https://platform-staging.bynry.com/sign-up")
driver.find_element(By.XPATH, "//*[@id=\"name\"]").send_keys("akash")
driver.find_element(By.XPATH, "//*[@id=\"email\"]").send_keys("akash124@yopmail.com")
driver.find_element(By.XPATH, "//*[@id=\"mobileNo\"]").send_keys("9561707877")

driver.find_element(By.XPATH, "//*[@id=\"orgName\"]").send_keys("UTILITY11")
dropdown = driver.find_element(By.XPATH, '//*[@class = "ant-form-item-control-input ng-tns-c630436078-6" or @class = "ant-form-item-control-input-content ng-tns-c630436078-6" or @class ="ant-select-selector ng-tns-c69490912-7"]')
# select = Select(static_dropdown)
# # select.select_by_visible_text('EV')


# Interact with the searchable dropdown
dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[contains(@class, "ant-select-selector")]'))
)
dropdown.click()  # Open the dropdown

# Enter search term in the dropdown's search field
search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[contains(@class, "ant-select-search__field")]'))
)
search_box.send_keys("Water")  # Type the search term

# Wait for the dropdown options to appear and select the correct one
option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "ant-select-item") and text()="Water"]'))
)
option.click()



# print(utility_services)
# for utility_service in utility_services:
#     if utility_service.text == "water":  # Replace "Option 5" with the desired option's text
#         utility_service.click()
#         print(utility_service.text)
#         break
