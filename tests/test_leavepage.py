from playwright.sync_api import sync_playwright, expect
from pages.login_page import LoginPage
from pages.navigation_page import NavigationPage
from pages.leave_page import LeavePage
from config import Config
from conftest import login 
import pytest

def test_leave_page(login):
    page = login
    nav = NavigationPage(page)
    nav.go_to_leave()

    leave_page = LeavePage(page)
    fromdate = "2026-01-01"
    todate = "2026-05-10"
    leave_type = "US - Personal"
    leave_page.search_myleave(fromdate,todate,leave_type)
    message = leave_page.get_toast_message()
    print(message)


