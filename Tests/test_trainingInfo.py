from playwright.sync_api import Page,expect
from Pages.training_info import TrainingInfoPage

def test_add_training(page: Page,login_credentials,training_data):
   
    training_page = TrainingInfoPage(page)
    
    
    training_page.navigate_to_login_page()
    training_page.login(
        username=login_credentials["username"],
        password=login_credentials["password"],
    )

   
    training_page.navigate_to_training_info()

    training_page.add_training(
        training_name=training_data["training_name"],        
        institute_name=training_data["institute_name"],          
        month_value = training_data["month_value"],    
        label = training_data["label"],    
             
    )

    expect(page.locator("text=Candidate Training Information added successfully.")).to_be_visible()