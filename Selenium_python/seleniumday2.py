from _multiprocessing import send
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#
# driver.find_element(By.XPATH,"//*[@id=\"name\"]").send_keys("nanji")  #for enter any name
# driver.find_element(By.XPATH,"//*[@id=\"name\"]").clear() #for enter any name
# driver.find_element(By.XPATH,"//*[@id=\"name\"]").send_keys("walzade")  #for enter any name

input_filed = driver.find_element(By.XPATH,"//*[@id=\"name\"]")
input_filed.clear()
alert_example = driver.find_element(By.XPATH,"//*[text()='Switch To Alert Example']")

alert_example_text = alert_example.text
print(alert_example_text)

