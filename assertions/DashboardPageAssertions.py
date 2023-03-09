from pageObjects.DashboardPage import DashboardPage

class DashboardPageAssertions(DashboardPage):
    
    def __init__(self,driver):
        self.driver=driver

    def checkLogoutbutton(self):
        assert self.driver.find_element(*DashboardPage.link_logout).text == "Logout", f"Getting error in check Logout"
