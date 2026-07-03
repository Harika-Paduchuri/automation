from playwright.sync_api import sync_playwright

class TimePage:
    def __init__(self,page):
        self.project_info_menu = page.locator("//span[normalize-space()='Project Info']//i[@class='oxd-icon bi-chevron-down']")
        self.customers = page.get_by_role("menuitem", name="Customers")
        self.add = page.get_by_role("button", name="Add")
        self.name = page.locator("//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']")
        self.description = page.get_by_role("textbox", name="Type description here")
        self.cancel = page.get_by_role("button", name="Cancel")
        self.save = page.get_by_role("button", name="Save")
        self.toast = page.locator(".oxd-toast-message")

    def add_customer(self,name,description):
        self.project_info_menu.click()
        self.customers.click()
        self.add.click()
        self.name.fill(name)
        self.description.fill(description)
        self.save.click()



