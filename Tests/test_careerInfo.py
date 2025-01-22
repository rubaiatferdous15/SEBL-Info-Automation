

from playwright.sync_api import Page, expect
from Pages.career_info import CareerInfoPage

def test_add_experience(page: Page,login_credentials,experience_info_data):

    experience_info_page = CareerInfoPage(page)

   
    experience_info_page.navigate_to_login_page()
    experience_info_page.login(
        username=login_credentials["username"],
        password=login_credentials["password"],
    )
    experience_info_page.navigate_to_career_info()
    experience_info_page.add_experience_info(
        experience_type=experience_info_data["experience_type"],
        employment_type=experience_info_data["employment_type"],
        started_as_mto=experience_info_data["started_as_mto"],
        skill=experience_info_data["skill"],
        organization=experience_info_data["organization"],
        designation=experience_info_data["designation"],
        joining_date=experience_info_data["joining_date"],
        end_date=experience_info_data["end_date"],
        job_description=experience_info_data["job_description"],
        desk_id=experience_info_data["desk_id"]
    )


    expect(page.locator("text=Candidate Experience added successfully.")).to_be_visible() 
