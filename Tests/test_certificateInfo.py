from playwright.sync_api import Page,expect
from Pages.certificate_info import CertificateInfoPage

def test_add_certificate(page: Page,login_credentials,certificate_data):
    certificate_page = CertificateInfoPage(page)
    
    
     
    certificate_page.navigate_to_login_page()
    certificate_page.login(
        username=login_credentials["username"],
        password=login_credentials["password"],
    )
 
    certificate_page.navigate_to_certificate_info()

   
    certificate_page.add_certification(
        certification_level=certificate_data["certification_level"],              
        certification_name=certificate_data["certification_name"],           
        institute_name=certificate_data["institute_name"],                 
        passing_year=certificate_data["passing_year"],                     
        month_value=certificate_data["month_value"], 
        label = certificate_data["label"],                
        file_path=  certificate_data["file_path"],     
                  
    )

    expect(page.locator("text=Candidate Certification added successfully.")).to_be_visible() 