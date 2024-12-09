import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()  # You can use ChromeDriver here
    driver.maximize_window()
    driver.get("https://example.com")  # Replace with the actual URL of your app
    request.cls.driver = driver
    yield
    driver.quit()
