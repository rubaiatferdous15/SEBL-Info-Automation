from playwright.sync_api import Page
from Pages.login_info import LoginPage

class BasicInfoPage(LoginPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.page.set_default_timeout(60000)
         
    def navigate_to_basic_info(self):
        
        self.page.get_by_role("link", name="Profile", exact=True).click()

        self.page.get_by_role("link", name="Basic Information").click() 

    def upload_files(self, image_file: str, cv_file: str, signature_file: str, freedom_fighter_file: str,):
        
        self.page.locator("input[name=\"image\"]").set_input_files(image_file)
        self.page.get_by_label("Upload CV:").set_input_files(cv_file)
        self.page.locator("input[name=\"signature\"]").set_input_files(signature_file)
        self.page.get_by_label("Are you eligible for freedom").check()
        self.page.get_by_label("Upload Freedom Fighter").set_input_files(freedom_fighter_file)
        
    def fill_personal_info(
        self,
        career_summary: str,
        first_name: str,
        last_name: str,
        father_name: str,
        mother_name: str,
        label: str,
        year: str,
        month: str,
        gender: str,
        marital_status: str,
        nationality: str,
        religion_id: str,
        nid_type_id: str,
        nid_number: str,
        blood_group_id: str,
        phone_number: str,
        
    ):
        self.page.get_by_placeholder("Enter Career Summary").fill(career_summary)
        self.page.get_by_placeholder("First Name").fill(first_name)
        self.page.get_by_placeholder("Last Name").fill(last_name)
        self.page.get_by_placeholder("Father Name").fill(father_name)
        self.page.get_by_placeholder("Mother Name").fill(mother_name)
        self.page.get_by_placeholder("Birth Date").click()
        self.page.get_by_label("Year").click()
        self.page.get_by_label("Year").fill(year)
        self.page.get_by_label("Month").select_option(month)
        self.page.get_by_label(label).click()
        self.page.locator(f"#{gender.capitalize()}").check()
        self.page.locator("#maritalStatusId").select_option(marital_status)
        self.page.get_by_placeholder("Nationality").fill(nationality)
        self.page.locator("#religionId").select_option(religion_id)
        self.page.get_by_label("NID/Smartcard Type:").select_option(nid_type_id)
        self.page.get_by_placeholder("NID/Smartcard Number").fill(nid_number)
        self.page.locator("#bloodGroupId").select_option(blood_group_id)
        self.page.locator("#phoneNumber").fill(phone_number)

    
        
    
    def fill_address_info(self, permanent_address: dict, present_address: dict):
        self.page.locator("#select2-permanentAddressCountryId-container").click()
        self.page.get_by_role("option", name=permanent_address["country"]).click()
        self.page.locator("#select2-permanentAddressDivisionId-container").click()
        self.page.get_by_role("option", name=permanent_address["division"]).click()
        self.page.locator("#select2-permanentAddressDistrictId-container").click()
        self.page.get_by_role("option", name=permanent_address["district"]).click()
        self.page.locator("#select2-permanentAddressThanaId-container").click()
        self.page.get_by_role("option", name=permanent_address["thana"]).click()
        self.page.locator("#permanentAddressLine1").fill(permanent_address["address_line"])
        self.page.locator("#select2-presentAddressDivisionId-container").click()
        self.page.get_by_role("option", name=present_address["division"]).click()
        self.page.locator("#select2-presentAddressDistrictId-container").click()
        self.page.get_by_role("option", name=present_address["district"]).click()
        self.page.locator("#select2-presentAddressThanaId-container").click()
        self.page.get_by_role("option", name=present_address["thana"]).click()
        self.page.locator("#presentAddressLine1").fill(present_address["address_line"])
        self.page.get_by_role("button", name="Save").click()

