from playwright.sync_api import Page, expect
from Pages.login_info import LoginPage  

class TrainingInfoPage(LoginPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.page.set_default_timeout(60000)
        
        
    def navigate_to_training_info(self):
        
        self.page.get_by_role("link", name="Profile", exact=True).click()
        
        self.page.get_by_role("link", name="Training Information").click()   
        
        



    def add_training(self, training_name: str, institute_name: str, month_value: str,label = str,):
      
        
        
        self.page.locator("a").filter(has_text="Add Training").click()
        
       
        self.page.get_by_role("textbox", name="Training Name").fill(training_name)
        
      
        self.page.get_by_role("textbox", name="Institute Name").fill(institute_name)
       
        self.page.get_by_role("textbox", name="Starts From").click()
        self.page.locator(".arrowDown").first.dblclick()  

        self.page.locator(".flatpickr-monthDropdown-months").nth(0).select_option(month_value) 
        self.page.get_by_label(label).click()  
      
        
        
        self.page.get_by_role("button", name="Save").click()
