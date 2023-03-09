from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from utilities.baseclass import BaseClass
import pytest

@pytest.fixture(scope='class')
def setup(request):
    browser = request.config.getoption("--browser")
    if browser=='chrome':
        driver=webdriver.Chrome(services=Service(ChromeDriverManager().install()))
    elif browser=='firefox':
        driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.maximize_window()
    driver.get("https://admin-demo.nopcommerce.com/")
    request.cls.driver = driver
    yield
    driver.save_screenshot(".//screenshots//"+"test_loginPageTitle.png")
    driver.close()
    driver.quit()
    
def pytest_addoption(parser):
    parser.addoption("--browser")


####### Pytest HTML Report #######

def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'QA_Tester_A'
