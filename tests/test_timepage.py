from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.navigation_page import NavigationPage
from pages.time_page import TimePage
from config import Config
from conftest import login
import pytest
import time

def test_time_page(login):
    page = login
    nav = NavigationPage(page)
    nav.go_to_time()

    time_page = TimePage(page)
    name = "manasa"
    description = "Associate QA Engineer"
    time_page.add_customer(name,description)
    
