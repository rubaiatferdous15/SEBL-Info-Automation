from playwright.sync_api import Page
from Pages.login_info import LoginPage 

class LogOutPage(LoginPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.page.set_default_timeout(60000)
        
    def logout(self):
        self.page.get_by_role("button", name="profile image").click()
        self.page.get_by_role("link", name="Logout").click()
