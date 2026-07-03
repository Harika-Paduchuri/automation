from playwright.sync_api import sync_playwright, expect
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.navigation_page import NavigationPage
from pages.pim_page import PimPage 
from config import Config
from conftest import login 
import pytest
import time

def test_pim_page(login):
    page = login
    nav = NavigationPage(page)
    nav.go_to_pim()

    pim = PimPage(page)
    image_path= r"C:\Users\Admin\Pictures\profile-icon-design-free-vector.jpg"

    employee_name="ahana"
    employee_id="0556"
    pim.add_employee("sunie","teja", "0992", image_path) 

    message = pim.get_toast_message()
    assert "Successfully Saved" in message
    print(message)

    nav.go_to_pim()
    pim.delete_employee(employee_name,employee_id)


