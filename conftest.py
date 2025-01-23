import pytest

# Login credentials
@pytest.fixture(scope="function")
def login_credentials():
    return {
        "username": "tamim@gmail.com",
        "password": "aaa"
    }

# Registration data
@pytest.fixture(scope="function")
def registration_data():
    return {
        "first_name": "John",
        "last_name": "Doe",
        "email": "newuser@example.com",
        "password": "Password123!"
    }
    
# Basic Information
@pytest.fixture(scope="function")
def basic_info_data():
    return {
        "image_file": "F:/SEBL Info Automation/Tests/Files/Image.jpg",
        "cv_file": "F:/SEBL Info Automation/Tests/Files/CV.pdf",
        "signature_file": "F:/SEBL Info Automation/Tests/Files/Sign.png",
        "career_summary": "Ambitious Driven",
        "first_name": "Tamim Iqbal",
        "last_name": "Iqbal Khan",
        "father_name": "Tanim Khan John doe",
        "mother_name": "Tania Khan Jane dowe",
        "label": "April 15,",
        "year": "2000",
        "month": "3",
        "gender": "Female",
        "marital_status": "1",
        "nationality": "Bangladeshi",
        "religion_id": "1",
        "nid_type_id": "1",
        "nid_number": "4040404040400",
        "blood_group_id": "4",
        "phone_number": "01732175344",
        "freedom_fighter_file": "F:/SEBL Info Automation/Tests/Files/CV.pdf",
        "permanent_address": {
            "country": "Bangladesh",
            "division": "Barisal",
            "district": "Barisal Sadar",
            "thana": "Bartonshire",
            "address_line": "Barishal",
        },
        "present_address": {
            "division": "Barisal",
            "district": "Barisal Sadar",
            "thana": "Bartonshire",
            "address_line": "Barishal",
        },
    }
# Career Information
@pytest.fixture(scope="function")
def experience_info_data():
    return {
        "experience_type": "1",  
        "employment_type": "1",  
        "started_as_mto": True,  
        "skill": "Testing",  
        "organization": "BRAC",  
        "designation": "INTERN",  
        "joining_date": {
            "month": "3", 
            "day": "April 15,",  
            "full_date": "2024-04-15"  
        },
        "end_date": {
            "month": "5",  
            "day": "June 1,",  
            "full_date": "2024-06-01"  
        },
        "job_description": "SA", 
        "desk_id": "4" 
    }


# Education information
@pytest.fixture(scope="function")
def education_info_data():
    return {
        "level": "5",  
        "degree_id": "26", 
        "subject_id": "1", 
        "institute_id": "196",  
        "grading_type_id": "1",  
        "grade": "3.73",  
        "out_of": "4.00",  
        "year": "2025" ,
        "file_path": "F:/SEBL Info Automation/Tests/Files/file.pdf"
    }

# Reference information
@pytest.fixture(scope="function")
def reference_data():
    return {
        "name": "Rubaiat Ahmed",
        "designation": "Lead QA",
        "institute_name": "REDDOT",
        "location": "Gulshan",
        "contact_no": "007",
        "email": "hejol@gmail.com",
        "relationship": "Mentor"
    }

# Training information
@pytest.fixture(scope="function")
def training_data():
    return {
        "training_name": "CSBT",
        "institute_name": "BRAC",
        "month_value": "3",
        "label": "April 1,"
    }
# Certificate information    
@pytest.fixture(scope="function")
def certificate_data():
    return{
        "certification_level" : "2",                
        "certification_name":"IT",               
        "institute_name":"BRAC",                 
        "passing_year":"2024",                   
        "month_value":"3", 
        "label":'April 15,',
        "file_path":"F:/SEBL Info Automation/Tests/Files/2mb.pdf"  
    }   

          
