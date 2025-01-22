from playwright.sync_api import Page, expect
from Pages.login_info import LoginPage  

class CertificateInfoPage(LoginPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.page.set_default_timeout(60000)
        
        
    def navigate_to_certificate_info(self):
        
        self.page.get_by_role("link", name="Profile", exact=True).click()
        
        self.page.get_by_role("link", name="Certification Information").click()       
        
    

    def add_certification(
        self,
        certification_level: str,
        certification_name: str,
        institute_name: str,
        passing_year: str,
        month_value: str,
        label = str,
        file_path =  str,
    ):
        self.page.locator("a").filter(has_text="Add Certification").click()
        self.page.locator("#bankingDiploma").check()
        self.page.locator("#certificationLevel").select_option(certification_level)
        self.page.get_by_role("textbox", name="Certification Name").fill(certification_name)
        self.page.get_by_role("textbox", name="Institute Name").fill(institute_name)
        self.page.get_by_role("textbox", name="Select Passing Year").click()
        self.page.get_by_role("option", name=passing_year).click()
        self.page.get_by_role("textbox", name="Achievement Date").click()
        self.page.locator(".arrowDown").first.click()
        self.page.get_by_label("Month").first.select_option(month_value)
        self.page.get_by_label(label).click()
        self.page.locator("#addNewCertificationForm div").filter(has_text="Upload Attachment/Certificate:").nth(2).click()
        self.page.locator("#addNewCertificationForm input[name=\"attachment\"]").set_input_files(file_path)
        self.page.get_by_role("button", name="Save").click()
