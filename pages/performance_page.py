from playwright.sync_api import sync_playwright

class PerformancePage:
    def __init__(self,page):
        self.my_tracker = page.get_by_text("My Trackers", exact=True)
        self.view = page.get_by_role("button", name="View")
        self.add_log = page.get_by_role("button", name="Add Log")
        self.log = page.locator("input[placeholder='Type here']")
        self.positive = page.get_by_role("button", name="Positive")
        self.negative = page.get_by_role("button", name="Negative")
        self.comment = page.locator("textarea.oxd-textarea.oxd-textarea--active.oxd-textarea--resize-vertical")
        self.cancel = page.get_by_role("button", name="Cancel")
        self.save = page.get_by_role("button", name="Save")

    def add_tracker_log(self, log, comment):
        self.my_tracker.click()
        self.view.click()
        self.add_log.click()
        self.log.fill(log)
        self.negative.click()
        self.comment.fill(comment)
        self.save.click()
