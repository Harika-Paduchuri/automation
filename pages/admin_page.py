from playwright.sync_api import sync_playwright, expect

class AdminPage:
    def __init__(self, page):
        self.page = page
        self.username = page.locator("//label[text()='Username']/ancestor::div[contains(@class,'oxd-input-group')]//input")
        self.user_role = page.locator("//label[normalize-space()='User Role']/ancestor::div[contains(@class,'oxd-input-group')]//div[contains(@class,'oxd-select-text-input')]")
        self.employee_name = page.get_by_role("textbox", name="Type for hints...")
        self.status = page.locator("//label[normalize-space()='Status']/ancestor::div[contains(@class,'oxd-input-group')]//div[contains(@class,'oxd-select-text-input')]")
        self.search_button = page.get_by_role("button", name="Search")
        self.reset_button = page.get_by_role("button", name="Reset")
        self.add_button = page.get_by_text("Add")
        self.records = page.locator(":text-is('(13) Records Found')")
        self.password = page.locator("//div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@type='password']")
        self.confirm_password = page.locator("//div[@class='oxd-grid-item oxd-grid-item--gutters']//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@type='password']")
        self.save_button = page.get_by_role("button", name="Save")
        self.employee_container = page.locator(".orangehrm-container")
        self.delete_icon = page.locator("div.oxd-table-cell-actions").locator("button").nth(0)

    def go_to_admin(self):
        self.page.get_by_role("link", name="Admin").click()

    def search_user(self, username, user_role, employee_name, status):
        self.username.fill(username)
        self.user_role.click()
        self.employee_name.fill(employee_name)
        self.status.click()
        self.search_button.click()

    def reset_search(self):
        self.reset_button.click()

    def click_add_user(self):
        self.add_button.click()

    def fill_user_details(self, username, user_role, status, password, confirm_password):

    # User Role
        self.user_role.click()
        self.page.get_by_role("option", name=user_role).click()

    # Employee Name
        self.employee_name.click()
        self.employee_name.fill("a")

        dropdown = self.page.locator(".oxd-autocomplete-dropdown")
        dropdown.wait_for(state="visible", timeout=5000)

        options = self.page.locator(".oxd-autocomplete-option")
        options.first.wait_for(state="visible", timeout=5000)
        options.first.click()

    # Status
        self.status.click()
        self.page.get_by_role("option", name=status).click()

    # Username
        self.username.fill(username)

    # Password
        self.password.fill(password)
        self.confirm_password.fill(confirm_password)

        

    def save_user(self):
        self.save_button.click()

    def add_new_user(self, username, user_role, status, password, confirm_password):
        self.click_add_user()
        self.fill_user_details(username, user_role, status, password, confirm_password)
        self.save_user()

    def delete_user(self, username):
        self.username.fill(username)
        self.search_button.click()
        self.delete_icon.click()


