from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, \
    ElementNotInteractableException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage(object): #Facade class to be used by all page objects
    errors = []
    def __init__(self, driver, explicit_wait=30):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, explicit_wait)
    
    
