from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.navigation_page import NavigationPage
from pages.performance_page import PerformancePage
from config import Config
from conftest import login
import pytest
import time

def test_performance_page(login):
    page = login
    nav = NavigationPage(page)
    nav.go_to_performance()

    performance_page = PerformancePage(page)
    log = "Automation Execution Log"
    comment = "Validated performance tracker log creation using automation script and confirmed data is saved successfully."
    performance_page.add_tracker_log(log,comment)
