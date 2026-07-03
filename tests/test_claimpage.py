from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.navigation_page import NavigationPage
from pages.claim_page import ClaimPage
from config import Config
from conftest import login
import pytest
import time

def test_claim_page(login):
    page = login
    nav = NavigationPage(page)
    nav.go_to_claim()

    claim_page = ClaimPage(page)
    event = "Travel Allowance"
    currency = "Indian Rupee"
    remarks = "Hotel expenses"
    expense_type = "Accommodation"
    date = "2026-26-06"
    amount = "1000"

    claim_page.create_claim(event, currency, remarks, expense_type, date, amount)
