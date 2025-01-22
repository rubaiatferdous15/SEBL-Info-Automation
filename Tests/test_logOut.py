from playwright.sync_api import Page,expect
from Pages.logout_info import LogOutPage

def test_logout(page: Page,login_credentials):

    logout_page = LogOutPage(page)
    
    logout_page.navigate_to_login_page()
    logout_page.login(
        username=login_credentials["username"],
        password=login_credentials["password"],
    )
    
    logout_page.logout()
    
    
    expect(page).to_have_url("https://sebl-career.leanhr.app/")