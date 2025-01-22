from playwright.sync_api import Page,expect
from Pages.reference_info import ReferenceInfoPage

def test_add_reference(page: Page,login_credentials,reference_data):
  

    # Navigate to Reference Information
    reference_page = ReferenceInfoPage(page)
    
    reference_page.navigate_to_login_page()
    reference_page.login(
        username=login_credentials["username"],
        password=login_credentials["password"],
    )

    reference_page.navigate_to_reference_info()

    # Add a new reference
    reference_page.add_reference(
        name=reference_data["name"],
        designation=reference_data["designation"],
        institute_name=reference_data["institute_name"],
        location=reference_data["location"],
        contact_no=reference_data["contact_no"],
        email=reference_data["email"],
        relationship=reference_data["relationship"],
    )

   
    expect(page.locator("text=Candidate reference added successfully.")).to_be_visible()

