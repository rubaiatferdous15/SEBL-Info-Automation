from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_field = page.get_by_placeholder("Enter Email")
        self.password_field = page.get_by_placeholder("Enter Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.page.set_default_timeout(60000)

    def navigate_to_login_page(self):
        self.page.goto("https://sebl-career.leanhr.app/users/candidate-login")

    def login(self, username: str, password: str):
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()
