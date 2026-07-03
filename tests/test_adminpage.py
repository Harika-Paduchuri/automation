from playwright.sync_api import sync_playwright, expect
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.navigation_page import NavigationPage
from pages.admin_page import AdminPage
from config import Config
from conftest import login 
import pytest
import time

@pytest.mark.regression
def test_admin_page(login):
    page = login
    nav = NavigationPage(page)
    nav.go_to_admin()

    admin_page = AdminPage(page)
    username = "Jobinsam@6742"
    admin_page.add_new_user("Sunitha","Admin","Enabled","Password123!","Password123!")
    

    nav.go_to_admin()
    admin_page.delete_user(username)

