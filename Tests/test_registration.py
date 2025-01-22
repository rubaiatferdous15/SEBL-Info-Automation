from playwright.sync_api import Page,expect

def test_user_registration(page: Page, registration_data):
    # Navigate to registration page
    page.goto("https://sebl-career.leanhr.app/")
    page.get_by_role("banner").click()
    page.get_by_role("link", name="Register").click()

    # Fill in registration data
    page.get_by_placeholder("Enter first name").fill(registration_data["first_name"])
    page.get_by_placeholder("Enter last name").fill(registration_data["last_name"])
    page.get_by_placeholder("Enter email address").fill(registration_data["email"])
    page.get_by_placeholder("Enter password").fill(registration_data["password"])
    page.get_by_placeholder("Confirm password").fill(registration_data["password"])
    page.get_by_label("By signing up you agree to").check()
   
    
    expect(page).to_have_url("https://sebl-career.leanhr.app/users/candidate-login")   
   


   
 
