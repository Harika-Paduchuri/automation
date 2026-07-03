from playwright.sync_api import sync_playwright, expect
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.navigation_page import NavigationPage
from conftest import login 
import time
import pytest

def test_search(login):
    page = login
    nav = NavigationPage(page)
    search_text = "main"
    nav.search(search_text)