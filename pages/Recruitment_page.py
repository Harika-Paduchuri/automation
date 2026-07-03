from playwright.sync_api import sync_playwright

class RecruitmentPage:
    def __init__(self,page):
        self.page = page
        self.candidates = page.get_by_role("link", name="Candidates")
        self.vacancies = page.locator("li:has-text('Vacancies')")
        self.job_title = page.locator("//label[text()='Job Title']/ancestor::div[contains(@class,'oxd-input-group')]//i")
        self.vacancy = page.locator("//label[text()='Vacancy']/ancestor::div[contains(@class,'oxd-input-group')]//i")
        self.hiring_manager = page.locator("//label[normalize-space()='Hiring Manager']/ancestor::div[contains(@class,'oxd-input-group')]//input")        
        self.status = page.locator("//label[text()='Status']/ancestor::div[contains(@class,'oxd-input-group')]//i")
        self.method_of_application = page.locator("//label[text()='Method of Application']/ancestor::div[contains(@class,'oxd-input-group')]//i")        
        self.search = page.get_by_role("button", name="Search")
        self.reset = page.get_by_role("button", name="Reset")
        self.toast = page.locator(".oxd-toast-content-text")
        self.no_search_results = page.locator("span").filter(has_text="No Records Found")

    def select_job_title(self, title):
        self.job_title.click()
        self.page.get_by_role("option", name=title).click()

    def select_vacancy(self, vacancy):
        self.vacancy.click()
        self.page.get_by_role("option", name=vacancy).click()

    def select_hiring_manager(self, hiring_manager):
        self.hiring_manager.click()
        self.page.get_by_role("option", name=hiring_manager).click()

    def select_status(self, status):
        self.status.click()
        self.page.get_by_role("option", name=status).click()

    def select_method_of_application(self, method_of_application):
        self.method_of_application.click()
        self.page.get_by_role("option", name=method_of_application).click()

    def click_search(self):
        self.search.click()

    def search_vacancies(self, title, vacancy, status):
        self.vacancies.click()
        self.select_job_title(title)
        self.select_vacancy(vacancy)
        self.select_status(status)
        self.click_search()  

    def search_candidates(self, title, vacancy, method_of_application):
        self.candidates.click()
        self.select_job_title(title)
        self.select_vacancy(vacancy)
        self.select_method_of_application(method_of_application)
        self.click_search()  
       
    def get_search_status(self):
        try:
            if self.no_search_results.is_visible():
                return self.toast.inner_text()
        except:
            pass

        return "Search results found"
  
    
        


