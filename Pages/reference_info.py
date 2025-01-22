from playwright.sync_api import Page
from Pages.login_info import LoginPage 

class ReferenceInfoPage(LoginPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.page.set_default_timeout(60000)

    def navigate_to_reference_info(self):
        self.page.get_by_role("link", name="Profile", exact=True).click()
        self.page.get_by_role("link", name="Reference Information").click()

    def add_reference(self, name: str, designation: str, institute_name: str, location: str, contact_no: str, email: str, relationship: str):
        self.page.locator("a").filter(has_text="Add Reference").click()
        self.page.get_by_role("textbox", name="Name", exact=True).fill(name)
        self.page.get_by_role("textbox", name="Designation").fill(designation)
        self.page.get_by_role("textbox", name="Working Institute Name").fill(institute_name)
        self.page.get_by_role("textbox", name="Working Location Address").fill(location)
        self.page.locator("#referenceContactNo").fill(contact_no)
        self.page.get_by_role("textbox", name="Email").fill(email)
        self.page.get_by_role("textbox", name="Relationship").fill(relationship)
        self.page.get_by_role("button", name="Save").click()
