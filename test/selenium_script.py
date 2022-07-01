from dataclasses import dataclass
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep 
from dataclasses import dataclass
from sentry_sdk import capture_message, capture_exception
import os 
from dotenv import load_dotenv
load_dotenv()
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration


sentry_sdk.init(
    dsn="https://b4f842a1561b40d9aa2056e45dddb116@o1297886.ingest.sentry.io/6527343",
    integrations=[
        FlaskIntegration(),
    ],
    traces_sample_rate=1.0
)



@dataclass
class Selenium_test:


    url = 'http://asp-ayoub-flaskapp.azurewebsites.net/' 
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def click_login_page(self):
        try : 
            self.driver.find_element(By.LINK_TEXT, 'Log in').click()
            assert self.driver.find_element(By.TAG_NAME, 'h1').text == 'Log in'
            capture_message('SELENIUM - SUCCESS : page login reached')
            print('Click to login sucess')
        except Exception as e :
            capture_message(f'SELENIUM - FAILED : page login not found -- error : {e}')
            print('No h1 found after click to login')
        print('------------------Test click on login page Done----------------------')
    
    def login_test(self, user, password) :
        # Insert user and password in the login form 
        self.driver.find_element(By.ID, 'email').send_keys(user)
        self.driver.find_element(By.ID , 'password').send_keys(password)
        sleep(1)
        self.driver.find_element(By.NAME, 'submit').click()
        
        # Assert h1 field is correct in this page
        try:
            h1 = self.driver.find_element( By.TAG_NAME, 'h1')
            assert h1.text == "Welwom to my website project"
            flash_login = self.driver.find_element(By.CLASS_NAME, 'alert')
            assert 'Logged in with success' in flash_login.text 
            capture_message('SELENIUM - SUCCESS : login done with sucess ')
        except Exception as e:
            print('ERROR ----- h1 not found after loging')
            capture_message(f'SELENIUM - FAILED : page login not found -- error : {e}')

        print('------------------test login user Done----------------------')

    def logout_test(self):
        self.driver.find_element(By.LINK_TEXT, 'Log out').click()
        try :
            flash_logout = self.driver.find_element(By.CLASS_NAME, 'alert')
            assert 'Vous êtes correctement déconnecté' in flash_logout.text 
            capture_message('SELENIUM - SUCCESS : login done with sucess ')
        except Exception as e:
            print('Alert info logout not in page')
            capture_message(f'SELENIUM - FAILED : page login not found -- error : {e}')

    def quit_test(self):
        self.driver.quit()


    def init_test(self):
        self.driver.get(self.url)
        self.click_login_page()
        self.login_test(os.getenv('USER_TESTING'), os.getenv('PASSWORD_TESTING'))
        self.logout_test()
        self.quit_test()



load_test = Selenium_test()
load_test.init_test()

