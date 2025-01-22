
from playwright.sync_api import Page, expect
from Pages.education_info import EducationInfoPage

def test_add_education_info(page: Page,login_credentials,education_info_data):
  

    education_info_page = EducationInfoPage(page)

    # Navigate and perform actions
    education_info_page.navigate_to_login_page()
    education_info_page.login(
        username=login_credentials["username"],
        password=login_credentials["password"],
    )
 
    education_info_page.navigate_to_education_info()
    education_info_page.add_education_info(
        level=education_info_data["level"],
        degree_id=education_info_data["degree_id"],
        subject_id=education_info_data["subject_id"],
        institute_id=education_info_data["institute_id"],
        grading_type_id=education_info_data["grading_type_id"],
        grade=education_info_data["grade"],
        out_of=education_info_data["out_of"],
        year=education_info_data["year"],
        file_path = education_info_data["file_path"],
    )


    expect(page.locator("text=Candidate education added successfully.")).to_be_visible()
