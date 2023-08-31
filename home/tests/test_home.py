from playwright.sync_api import Page, expect

def test_homepage_with_playwright(page: Page):
    page.goto("http://localhost:8000")
    expect(page).to_have_title("Home")
    expect(page.get_by_text("Welcome to your new Wagtail site!")).to_be_visible()