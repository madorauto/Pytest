from selenium.webdriver.common.by import By

class DashboardPage:
    link_logout = (By.LINK_TEXT, "Logout")
    
    def getLogOut(self):
        return  self.driver.find_element(*self.link_logout)