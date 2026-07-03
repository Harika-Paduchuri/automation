from playwright.sync_api import sync_playwright

class MaintenancePage:
    def __init__(self,page):
        self.page = page
        self.heading = page.get_by_role("heading", name="Administrator Access")
        self.password = page.locator('[name="password"]')
        self.error_message = page.get_by_text("Invalid credentials", exact=True)
        self.confirm = page.get_by_role("button", name="Confirm")

    def verify_access(self,password):
        self.password.fill(password)
        self.confirm.click()
        