from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
check_boxes = driver.find_elements(By.XPATH,"//*[starts-with(@name,'checkBoxOption')]")
print(check_boxes)
print(len(check_boxes))


# for loop

for check_boxe in check_boxes:
    check_boxe.click()



#
#
# # if i have 7 check boxes but need to check only 6
#
# for checkboxes in checkboxes:
#     if checkboxes.index(checkboxes)+1<7:
#         checkboxes.click()