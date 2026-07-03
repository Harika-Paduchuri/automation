from playwright.sync_api import sync_playwright

class NavigationPage:

    def __init__(self, page):
        self.page = page
        self.side_pannel = page.locator(".oxd-navbar-nav")
        self.searchbar = page.get_by_placeholder("Search")

    def search(self,search_text):
        self.searchbar.fill(search_text)
        results = self.page.locator(".oxd-main-menu-item")
        for i in range(results.count()):
            result_text = results.nth(i).text_content().strip()
        if  search_text.lower() in result_text.lower():            
            results.click()
        else:
            print("wrong entry")


    def click_menu(self, menu_name):
        self.page.get_by_role("link", name=menu_name).click()

    def go_to_admin(self):
        self.click_menu("Admin")
    
    def go_to_pim(self):
        self.click_menu("PIM")

    def go_to_leave(self):
        self.click_menu("Leave")

    def go_to_time(self):
        self.click_menu("Time")

    def go_to_recruitment(self):
        self.click_menu("Recruitment") 

    def go_to_my_info(self):
        self.click_menu("My Info") 

    def go_to_performance(self):
        self.click_menu("Performance")

    def go_to_dashboard(self):
        self.click_menu("Dashboard")
    
    def go_to_directory(self):
        self.click_menu("Directory")

    def go_to_maintenance(self):
        self.click_menu("Maintenance")

    def go_to_claim(self):
        self.click_menu("Claim")

    def go_to_buzz(self):
        self.click_menu("Buzz")

  