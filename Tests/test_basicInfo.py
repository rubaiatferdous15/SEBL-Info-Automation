from playwright.sync_api import Page, expect
from Pages.basic_info import BasicInfoPage

def test_basic_info(page: Page,login_credentials, basic_info_data):
    
    

    
    basic_info_page = BasicInfoPage(page)

  
    basic_info_page.navigate_to_login_page()
    basic_info_page.login(
        username=login_credentials["username"],
        password=login_credentials["password"],
    )
    basic_info_page.navigate_to_basic_info()
 
    basic_info_page.upload_files(image_file = basic_info_data["image_file"],
    cv_file = basic_info_data["cv_file"],
    signature_file = basic_info_data["signature_file"],
   
    freedom_fighter_file = basic_info_data["freedom_fighter_file"],)
    basic_info_page.fill_personal_info( career_summary = basic_info_data["career_summary"],
    first_name = basic_info_data["first_name"],
    last_name = basic_info_data["last_name"],
    father_name = basic_info_data["father_name"],
    mother_name = basic_info_data["mother_name"],
    label = basic_info_data["label"],
    year = basic_info_data["year"],
    month = basic_info_data["month"],
    gender = basic_info_data["gender"],
    marital_status = basic_info_data["marital_status"],
    nationality = basic_info_data["nationality"],
    religion_id = basic_info_data["religion_id"],
    nid_type_id = basic_info_data["nid_type_id"],
    nid_number = basic_info_data["nid_number"],
    blood_group_id = basic_info_data["blood_group_id"],
    phone_number = basic_info_data["phone_number"],)
    basic_info_page.fill_address_info(permanent_address = basic_info_data["permanent_address"],
    present_address = basic_info_data["present_address"],)

   
    expect(page.locator("text=Candidate profile updated successfully.")).to_be_visible()
