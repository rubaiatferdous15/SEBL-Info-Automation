from playwright.sync_api import Page,expect
from Pages.login_info import LoginPage

def test_login_valid_credentials(page: Page, login_credentials):
    # Initialize the LoginPage class
    login_page = LoginPage(page)

    # Navigate to the login page
    login_page.navigate_to_login_page()

    # Perform login using credentials from the fixture
    login_page.login(
        username=login_credentials["username"],
        password=login_credentials["password"],
    )

    
    expect(page).to_have_url("https://sebl-career.leanhr.app/candidate/dashboard")   
  