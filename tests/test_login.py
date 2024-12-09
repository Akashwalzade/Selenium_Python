import pytest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("test_user")
        login_page.enter_password("test_password")
        login_page.click_login()

        # Assert that the login was successful (example check)
        assert "Dashboard" in self.driver.title, "Login failed!"
