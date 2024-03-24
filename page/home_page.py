from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from base.base_page import BasePage
from page.career_page import CareerPage

class HomePage(BasePage):
    menu = (By.ID,'navbarDropdownMenuLink')
    dropdown_menu = (By.CLASS_NAME,'dropdown-sub')
    cookies = (By.ID,'wt-cli-reject-btn')

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_page_load()
    
    def wait_page_load(self):
        self.wait.until(ec.visibility_of_element_located(self.cookies))

    def close_cookies(self):
        self.driver.find_element(*self.cookies).click()
    
    def menu_click(self,name):
        elements = self.driver.find_elements(*self.menu)
        [i for i in elements if i.text==name][0].click()
    
    def dropdown_click(self,name):
        elements = self.driver.find_elements(*self.dropdown_menu)
        [i for i in elements if i.text==name][0].click()
        return CareerPage(self.driver)

        


