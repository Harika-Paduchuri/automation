from playwright.sync_api import sync_playwright

class ClaimPage:
    def __init__(self,page):
        self.page = page
        self.my_claim = page.get_by_role("link", name="My Claims")
        self.reference_id =page.get_by_role("textbox", name="Type for hints...")
        self.event_name = page.locator("//div[@class='oxd-table-filter-area']//div[2]//div[1]//div[2]//div[1]//div[1]//div[2]//i[1]")
        self.status = page.locator("//div[3]//div[1]//div[2]//div[1]//div[1]//div[2]//i[1]")
        self.from_date = page.locator("//label[text()='From Date']/ancestor::div[contains(@class,'oxd-input-group')]//input")
        self.to_date = page.locator("//label[text()='To Date']/ancestor::div[contains(@class,'oxd-input-group')]//input")
        self.search = page.get_by_role("button", name="Search")
        self.reset = page.get_by_role("button", name="Reset")
        self.submit_claim = page.get_by_role("button", name="Submit Claim")
        self.event_dropdown = page.locator("//label[text()='Event']/ancestor::div[contains(@class,'oxd-input-group')]//div[@class='oxd-select-text oxd-select-text--active']")        
        self.currency_dropdown = page.locator("//label[text()='Currency']/ancestor::div[contains(@class,'oxd-input-group')]//div[@class='oxd-select-text oxd-select-text--active']")        
        self.remarks = page.locator("textarea.oxd-textarea.oxd-textarea--active.oxd-textarea--resize-vertical")
        self.create = page.get_by_role("button", name="Create")
        self.cancel = page.get_by_role("button", name="Cancel")
        self.add = page.locator("button").filter(has_text="Add").first
        self.expense_type = page.locator("i.oxd-icon.bi-caret-down-fill.oxd-select-text--arrow")
        self.date = page.get_by_role("textbox", name="yyyy-dd-mm")
        self.amount = page.locator("//label[text()='Amount']/ancestor::div[contains(@class,'oxd-input-group')]//input")        
        self.note = page.get_by_label("Note")
        self.save = page.get_by_role("button", name="Save")
        self.cancel = page.locator("button").filter(has_text="Cancel").first
        self.submit = page.get_by_role("button", name="Submit")
    
    def create_claim(self, event, currency, remarks, expense_type, date, amount):
        self.my_claim.click()
        self.submit_claim.click()
        self.event_dropdown.click()
        self.page.get_by_role("option", name=event).click()
        self.currency_dropdown.click()
        self.page.get_by_role("option", name=currency).click()
        self.remarks.fill(remarks)
        self.create.click()
        self.add.click()
        self.expense_type.click()
        self.page.get_by_role("option", name=expense_type).click()
        self.date.fill(date)
        self.amount.fill(amount)
        self.save.click()
        self.submit.click()


