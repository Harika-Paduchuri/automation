from playwright.sync_api import sync_playwright, expect
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.navigation_page import NavigationPage
from pages.maintenance_page import MaintenancePage
from conftest import login 
import time
import pytest

def test_maintenance_page(login):
    page = login
    nav = NavigationPage(page)
    nav.go_to_maintenance()

    maintenance_page = MaintenancePage(page)
    password = "admin@123"
    maintenance_page.verify_access(password)
    expect(maintenance_page.error_message).to_be_visible()
    print(maintenance_page.error_message.inner_text())