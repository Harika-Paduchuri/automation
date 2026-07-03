from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.navigation_page import NavigationPage
from pages.Recruitment_page import RecruitmentPage
from config import Config
from conftest import login
import pytest
import time

def test_recruitment_page(login):
    page = login
    nav = NavigationPage(page)
    nav.go_to_recruitment()
    recruitment = RecruitmentPage(page)
    title = "Payroll Administrator"
    vacancy = "Payroll Administrator"
    status = "Closed"
    method_of_application = "online"
    recruitment.search_vacancies(title, vacancy, status)
    print(recruitment.get_search_status())

    recruitment.search_candidates(title, vacancy, method_of_application)
    print(recruitment.get_search_status())
