import pytest
from assertions.DashboardPageAssertions import DashboardPageAssertions
from assertions.LoginPageAssetions import LoginPageAssertions
from pageObjects.LoginPage import LoginPage
from pageActions.LoginPageActions import LoginPageActions
from testData.LoginPageData import LoginPageData
from utilities.baseclass import BaseClass

class Test_001_Login(BaseClass):
    
    def test_loginPageTitle(self):
        log = self.getLogger()
        log.info("***** Test_001_Login *****")
        log.info("***** Verifying Login Page Title *****")
        self.lp=LoginPageAssertions(self.driver)
        self.lp.checkLoginHeaderTitle()
        log.info("***** Login page test is passed *****")

    def test_valid_login(self):
        log = self.getLogger()
        log.info("***** Verifying Login Test *****")
        self.lp=LoginPageActions(self.driver)
        self.dpa=DashboardPageAssertions(self.driver)
        self.lp.inputUsername(LoginPageData.username)
        self.lp.inputPassword(LoginPageData.password)
        self.lp.clickLogin()
        self.dpa.checkLogoutbutton()
        log.info("***** Login test is passed *****")

    def test_invalid_login(self):
        log = self.getLogger()
        log.info("***** Verifying Invalid Login Test *****")
        self.Action=LoginPageActions(self.driver)
        self.Validation=LoginPageAssertions(self.driver)
        self.Action.inputUsername(LoginPageData.invalidusername)
        self.Action.inputPassword(LoginPageData.invalidpassword)
        self.Action.clickLogin()
        self.Validation.checkErrorMessage(LoginPageData.genericloginerrormessage)
        self.Validation.checkErrorMessage(LoginPageData.usernameerrormessage)
        self.Action.inputUsername(LoginPageData.invalidusername)
        self.Action.inputPassword(LoginPageData.password)
        self.Action.clickLogin()
        self.Validation.checkErrorMessage(LoginPageData.genericloginerrormessage)
        self.Validation.checkErrorMessage(LoginPageData.usernameerrormessage)
        self.Action.inputUsername(LoginPageData.username)
        self.Action.inputPassword(LoginPageData.invalidpassword)
        self.Action.clickLogin()
        self.Validation.checkErrorMessage(LoginPageData.genericloginerrormessage)
        self.Validation.checkErrorMessage(LoginPageData.passworderrormessage)
        self.Action.inputUsername(LoginPageData.username)
        self.Action.inputPassword(LoginPageData.blankpassword)
        self.Action.clickLogin()
        self.Validation.checkErrorMessage(LoginPageData.genericloginerrormessage)
        self.Validation.checkErrorMessage(LoginPageData.passworderrormessage)
        self.Action.inputUsername(LoginPageData.blankusername)
        self.Action.inputPassword(LoginPageData.password)
        self.Validation.checkEmailErrorMessage(LoginPageData.emailerrormessage)
        log.info("***** Invalid Login test is passed *****")