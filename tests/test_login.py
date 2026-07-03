from playwright.sync_api import sync_playwright, expect
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.navigation_page import NavigationPage
from config import Config
import pytest
import time
import json

with open("testdata/login_data.json", "r")as f:
        data = json.load(f) 

@pytest.mark.regression

def test_valid_login(page):
    page.goto(Config.BASE_URL) 
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    nav = NavigationPage(page)
    #login_page.valid_login(Config.USERNAME, Config.PASSWORD)
    valid_user=data["valid_user"]
    login_page.valid_login(
        valid_user["username"],
        valid_user["password"]
    )
    # Wait for the dashboard header to be visible
    expect(login_page.dashboard_header).to_be_visible(timeout=5000)  # Wait up to 5 seconds

    #nav.click_menu("PIM")  
    #or 
    nav.go_to_pim()

    
    #to perform logout action
    dashboard_page.logout()




