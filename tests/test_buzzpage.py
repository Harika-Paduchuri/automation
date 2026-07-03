from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.navigation_page import NavigationPage
from pages.buzz_page import BuzzPage
from conftest import login 
import time
import pytest

def test_buzz_page(login):
    page = login
    nav = NavigationPage(page)
    nav.go_to_buzz()

    buzz_page = BuzzPage(page)
    text_post = "Hello Everyone, This is Robot 2.0"
    path = r"C:\Users\Admin\Pictures\download.gif"
    v_path = r"https://www.youtube.com/watch?v=VHwl78QXF_0&list=PLUDwpEzHYYLtFprdVOrMLBJcqCJ-gRDYa"
    buzz_page.post_text(text_post)
    buzz_page.post_image(path)
    buzz_page.post_video(text_post,v_path)
    
    