from playwright.sync_api import sync_playwright

class LeavePage:
    def __init__(self,page):
        self.page = page
        self.leave_page_header = page.locator(".oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module")
        self.myleave_menu = page.get_by_text("My Leave", exact=True)
        self.fromdate = page.locator("//div[@class='oxd-grid-4 orangehrm-full-width-grid']//div[1]//div[1]//div[2]//div[1]//div[1]//input[1]")
        self.todate = page.locator("//div[@class='oxd-grid-4 orangehrm-full-width-grid']//div[1]//div[1]//div[2]//div[1]//div[1]//input[1]")
        self.leave_type = page.locator("//div[@class='oxd-select-wrapper']//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']")
        self.reset = page.get_by_role("button", name="Reset")
        self.search = page.get_by_role("button", name="Search")
        self.toast = page.locator("#oxd-toaster_1")
    
    def search_myleave(self,fromdate,todate, leave_type):
        self.myleave_menu.click()
        self.fromdate.fill(fromdate)
        self.todate.fill(todate)
        self.leave_type.click()
        self.page.get_by_text(leave_type, exact=True).click()
        self.search.click()
    

    def get_toast_message(self):
        self.toast.wait_for(state="visible", timeout=5000)
        return self.toast.inner_text()

