# login_page.py
# =====================
# This class represents the "Login Page" of the application.
# It is designed using the Page Object Model (POM) pattern,
# which helps to keep locators and actions separate from the test logic.

from playwright.sync_api import sync_playwright 

class LoginPage:

    def __init__(self, page):
        self.page = page
        # Define locators for the login page elements
        self.username = page.get_by_placeholder("Username")
        self.password = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.locator(".oxd-alert--error") 
        self.forgot_password= page.locator(".orangehrm-login-forgot-header") 
        self.dashboard_header = page.get_by_role("heading", name="Dashboard")

    def valid_login(self, username, password):
        """Perform a valid login action."""
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

    def invalid_login(self, username, password):
        """Perform an invalid login action."""
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

    def get_error_message(self):
        try:
            return self.error_message.text_content()
        except Exception as e:
            print(f"Exception while fetching login error message: {e}")
            return None   
    
    def dashboard_header_visible(self):
        return self.dashboard_header.is_visible()
