from playwright.sync_api import Page

class RegistrationPage:
    def __init__(self, page: Page):
        self.page = page
        self.page.set_default_timeout(60000)
        
    def navigate_to_registration_page(self):
        self.page.goto("https://sebl-career.leanhr.app/")
        self.page.get_by_role("banner").click()
        self.page.get_by_role("link", name="Register").click()

    def register_user(self, first_name: str, last_name: str, email: str, password: str):
        self.page.get_by_placeholder("Enter first name").click()
        self.page.get_by_placeholder("Enter first name").fill(first_name)

        self.page.get_by_placeholder("Enter last name").click()
        self.page.get_by_placeholder("Enter last name").fill(last_name)

        self.page.get_by_placeholder("Enter email address").click()
        self.page.get_by_placeholder("Enter email address").fill(email)

        self.page.get_by_placeholder("Enter password").click()
        self.page.get_by_placeholder("Enter password").fill(password)

        self.page.get_by_placeholder("Confirm password").click()
        self.page.get_by_placeholder("Confirm password").fill(password)

        self.page.get_by_label("By signing up you agree to").check()
        # self.page.get_by_role("button", name="Create Account").click()
