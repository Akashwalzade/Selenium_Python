from selenium import webdriver
from selenium.webdriver.common.by import By

# CSS selectors
# Class >>   tagname.classvalue   (Tagname is optional)
# ID >>      Tagname#IDvalue  ex>>
# Attribute & Value >> tagname[attribute ='value']
# class,Attribute & Value >> tagname.classvalue[attribute ='value']

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")


