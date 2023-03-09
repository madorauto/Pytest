from pageObjects.LoginPage import LoginPage

class LoginPageActions(LoginPage):

    def __init__(self,driver):
        self.driver=driver

    def inputUsername(self,username):
        self.driver.find_element(*LoginPage.textbox_username).clear()
        self.driver.find_element(*LoginPage.textbox_username).send_keys(username)

    def inputPassword(self,password):
        self.driver.find_element(*LoginPage.textbox_password).clear()
        self.driver.find_element(*LoginPage.textbox_password).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(*LoginPage.button_submit).click()