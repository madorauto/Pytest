from pageObjects.LoginPage import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPageAssertions(LoginPage):
    
    def __init__(self,driver):
        self.driver=driver

    def checkLoginHeaderTitle(self):
        assert self.driver.find_element(*LoginPage.text_login).text == "Admin area demo", f"Getting error in check Logout"

    def checkErrorMessage(self,errorMessage):
        getErrorMsg = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((self.error_message)))
        assert errorMessage in getErrorMsg.text, f"Getting error in error message"

    def checkEmailErrorMessage(self,errorMessage):
        getErrorMsg = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((self.email_error_message)))
        assert errorMessage in getErrorMsg.text, f"Getting error in email error message"