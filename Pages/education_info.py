from playwright.sync_api import Page, expect
from Pages.login_info import LoginPage  

class EducationInfoPage(LoginPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.page.set_default_timeout(60000)
        
        
    def navigate_to_education_info(self):
        self.page.get_by_role("link", name="Profile", exact=True).click()
        
        self.page.get_by_role("link", name="Education Information").click()
        

    def add_education_info(self, level: str, degree_id: str, subject_id: str, 
                           institute_id: str, grading_type_id: str, grade: str, 
                           out_of: str, year: str,file_path:str):
        # Open Add Education Form
        self.page.locator("a").filter(has_text="Add Education").click()

        # Select Education Level
        self.page.locator("#educationLevel").select_option(level)

        # Select Degree
        self.page.locator("#educationDegreeId").select_option(degree_id)

        # Select Subject
        self.page.locator("#educationSubjectId").select_option(subject_id)

        # Select Institute
        self.page.locator("#educationInstituteId").select_option(institute_id)

        # Select Grading System
        self.page.locator("#educationGradingType").select_option(grading_type_id)

        # Fill Grade
        self.page.get_by_role("textbox", name="Grade").click()
        self.page.get_by_role("textbox", name="Grade").fill(grade)

        # Fill Out of
        self.page.get_by_role("textbox", name="Out of").click()
        self.page.get_by_role("textbox", name="Out of").fill(out_of)

        # Select Passing Year
        self.page.locator("#educationYearId").select_option(year)
        
        self.page.locator("#addNewEducationForm input[name=\"attachment\"]").click()
        self.page.locator("#addNewEducationForm input[name=\"attachment\"]").set_input_files(file_path)
        self.page.get_by_role("button", name="Save").click()