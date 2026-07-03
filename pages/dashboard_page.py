from playwright.sync_api import sync_playwright 

class DashboardPage: 
    def __init__(self, page):
        self.page = page
        self.dashboard_header = page.get_by_role("heading", name="Dashboard")
        self.profile_menu = page.locator(".oxd-userdropdown-name")
        self.logout_button = page.get_by_role("menuitem", name="Logout")
        self.login_message = page.get_by_role("heading", name="Login")

    def logout(self):
        self.profile_menu.click()
        self.logout_button.click()
        
    def login_message_visible(self):
        return self.login_message.is_visible()