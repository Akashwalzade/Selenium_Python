from selenium import webdriver


# attribute & value = //tagname[@attribute='value'] also //*[@attribute='value']
#
# 2 attribute & values = //tagname[@attribute='value' and/or @attribute='value']
#
# text = //tagname[text()='type txt here']


driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.find_element()
#
# //input[@value='radio2' and @name='radioButton' or @class='radiobutton']
#
# //*[text()='Suggession Class Example']
#
# //*[starts-with(@value,'rad')] >> starting with
#
# //*[contains(@value,'ad')] >> mid value
#
# //input[@value='radio2']
#
# parent to child
# //div[@id='radio-btn-example']/fieldset/label[@for='radio3']
#
# relative xpath > / single start from root and that is called (parent to child)
# absolute xpath > // double start or directely find absolute value (any mid value)

