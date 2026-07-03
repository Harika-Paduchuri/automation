from playwright.sync_api import sync_playwright 

class PimPage:

    def __init__(self, page):
        self.page = page
        self.employee_list_header = page.get_by_role("link", name="Employee List")
        self.add = page.get_by_role("button", name="Add")
        self.first_name = page.locator(".orangehrm-firstname")
        self.middle_name = page.get_by_role("textbox", name="Middle Name")
        self.last_name = page.get_by_role("textbox", name="Last Name")
        self.employee_id = page.locator("//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']")
        self.employee_image = page.locator("button.oxd-icon-button.oxd-icon-button--solid-main.employee-image-action")
        self.save = page.get_by_role("button", name="Save")
        self.cancel = page.get_by_role("button", name="Cancel")
        self.toast = page.locator(".oxd-toast-container--bottom")
        self.employee_name = page.locator("//div[@class='oxd-grid-4 orangehrm-full-width-grid']//div[1]//div[1]//div[2]//div[1]//div[1]//input[1]")
        self.search = page.get_by_role("button", name="Search")
        self.employee_id = page.locator("//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']")
        self.delete = page.locator("div.oxd-table-cell-actions").locator("button").nth(1)
        self.confirm_delete = page.get_by_role("button", name="Yes, Delete")

    def add_employee(self, first_name, last_name, employee_id, image_path):
        self.add.click()
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.employee_id.fill(employee_id)

        with self.page.expect_file_chooser() as fc:
            self.employee_image.click()
            fc.value.set_files(image_path)

        self.save.click()

    def get_toast_message(self):
        self.toast.wait_for(state="visible", timeout=5000)
        return self.toast.inner_text()

    def delete_employee(self,employee_name,employee_id):
        self.employee_name.fill(employee_name)
        self.employee_id.fill(employee_id)
        self.search.click()
        self.delete.click()
        self.confirm_delete.click()




        
    