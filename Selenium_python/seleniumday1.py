

from selenium import webdriver
# from selenium.webdriver.chrome.service import service (use for the webdriver url) >> before 4.6 selenium version
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)

# to update drivers default behaviour

# class By:
#     """Set of supported locator strategies."""
#
#     ID = "id"
#     XPATH = "xpath"
#     LINK_TEXT = "link text"
#     PARTIAL_LINK_TEXT = "partial link text"
#     NAME = "name"
#     TAG_NAME = "tag name"
#     CLASS_NAME = "class name"
#     CSS_SELECTOR = "css selector"

driver = webdriver.Chrome(options=options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.ID, "checkBoxOption1").click()
driver.find_element(By.NAME, "checkBoxOption2").click()

driver.find_element(By.CLASS_NAME, "checkBoxOption3").click()
