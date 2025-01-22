from playwright.sync_api import Page, expect
from Pages.login_info import LoginPage  

class CareerInfoPage(LoginPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.page.set_default_timeout(60000)
        
    def navigate_to_career_info(self):
        
        self.page.get_by_role("link", name="Profile", exact=True).click()

        self.page.get_by_role("link", name="Career Information").click()   


    def add_experience_info(self, experience_type: str, employment_type: str, 
                            started_as_mto: bool, skill: str, organization: str, 
                            designation: str, joining_date: str, end_date: str, 
                            job_description: str, desk_id: str):
        # Open Add Experience Form
        self.page.locator("#experienceSection").get_by_text("Add Experience").click()

        # Select Experience Type
        self.page.locator("#experienceType").select_option(experience_type)

        # Select Employment Type
        self.page.locator("#employmentType").select_option(employment_type)

        # Check 'Started As MTO?'
        if started_as_mto:
            self.page.get_by_role("checkbox", name="Started As MTO?").check()

        # Select Skill
        self.page.locator(".select2-selection").click()
        self.page.get_by_role("option", name=skill).click()

        # Select Additional Skill
        self.page.locator("#select2-skills-container").click()
        self.page.get_by_role("option", name="Accounts", exact=True).click()

        # Fill Organization Name
        self.page.get_by_label("Organization Name:").click()
        self.page.get_by_label("Organization Name:").fill(organization)

        # Fill Current/Last Designation
        self.page.get_by_placeholder("Current/Last Designation").click()
        self.page.get_by_placeholder("Current/Last Designation").fill(designation)

        # Fill Joining Designation
        self.page.get_by_label("Joining Designation:").click()
        self.page.get_by_label("Joining Designation:").fill(designation)

        # Select Desk ID
        self.page.locator("#deskId").select_option(desk_id)

        # Fill Joining Date
        self.page.get_by_role("textbox", name="Joining Date").click()
        self.page.locator("div:nth-child(14) > .flatpickr-wrapper > .flatpickr-calendar > .flatpickr-months > .flatpickr-month > .flatpickr-current-month > .numInputWrapper > .arrowDown").click()
        self.page.get_by_label("Month").nth(1).select_option(joining_date["month"])
        self.page.get_by_label(joining_date["day"]).click()
        

        # Fill End Date
        self.page.get_by_role("textbox", name="End Date").click()
        self.page.locator("div:nth-child(15) > .flatpickr-wrapper > .flatpickr-calendar > .flatpickr-months > .flatpickr-month > .flatpickr-current-month > .numInputWrapper > .arrowDown").click()
        self.page.get_by_label("Month").nth(2).select_option(end_date["month"])
        self.page.get_by_label(end_date["day"]).click()
       

        # Fill Job Description
        self.page.get_by_label("Job Description:").click()
        self.page.get_by_label("Job Description:").fill(job_description)
        self.page.get_by_role("button", name="Save").click()

        
        

  