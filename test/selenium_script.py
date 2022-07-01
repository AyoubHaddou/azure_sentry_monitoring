from dataclasses import dataclass
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep 
from dataclasses import dataclass
import os 
from dotenv import load_dotenv
load_dotenv()


@dataclass
class Selenium_test:


    url = 'http://asp-ayoub-flaskapp.azurewebsites.net/' 
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def click_login_page(self):
        login_button = self.driver.find_element(By.LINK_TEXT, 'Log in').click()
        print('------------------Test click on login page Done----------------------')
    
    def login_test(self, user, password) :
        # Insert user and password in the login form 
        self.driver.find_element(By.ID, 'email').send_keys(user)
        self.driver.find_element(By.ID , 'password').send_keys(password)
        sleep(1)
        self.driver.find_element(By.NAME, 'submit').click()
        
        # Assert h1 field is correct in this page
        # Try + assert ou l'un ou l'autre uniquement ? 
        try:
            h1 = self.driver.find_element( By.TAG_NAME, 'h1')
            assert h1.text == "Welwom to my website project"
        except AttributeError:
            print('ERROR ----- h1 not found after loging')
        # Assert Flash login success 
        flash_login = self.driver.find_element(By.CLASS_NAME, 'alert')
        assert 'Logged in with success' in flash_login.text 
        print('------------------test login user Done----------------------')

    def logout_test(self):
        self.driver.find_element(By.LINK_TEXT, 'Log out').click()
        try :
            flash_logout = self.driver.find_element(By.CLASS_NAME, 'alert')
            assert 'Vous êtes correctement déconnecté' in flash_logout.text 
        except AttributeError:
            print('Alert info logout not in page')

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

