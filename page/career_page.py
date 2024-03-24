from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from base.base_page import BasePage
from selenium.common.exceptions import * 
from page.qa_page import QaPage
# from page.career_page 

class CareerPage(BasePage):
    menu = (By.ID,'navbarDropdownMenuLink')
    dropdown_menu = (By.CLASS_NAME,'dropdown-sub')
    teams = (By.ID,'career-find-our-calling')
    locations = (By.ID,'career-our-location')
    life_insider = (By.XPATH,'/html/body/div[1]/section[4]')
    sat_btn = (By.CLASS_NAME,'btn btn-outline-secondary rounded text-medium mt-5 mx-auto py-3 loadmore')

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_page_load()
    
    def wait_page_load(self):
        self.wait.until(ec.visibility_of_element_located(self.teams))
    
    def life_insider_loaded(self):
        text = 'Life at İnsider'
        try:
            element = self.driver.find_element(*self.life_insider)
            print(f'{text} loaded')
        except NoSuchElementException:
            self.errors.append(f'{text} not found')
    
    def teams_loaded(self):
        text = 'Teams'
        try:
            element = self.driver.find_element(*self.teams)
            print(f'{text} loaded')
        except NoSuchElementException:
            self.errors.append(f'{text} not found')
    
    def locations_loaded(self):
        text = 'Locations'
        try:
            element = self.driver.find_element(*self.locations)
            print(f'{text} loaded')
        except NoSuchElementException:
            self.errors.append(f'{text} not found')
    
    def qa_page(self):
        qa_url = 'https://useinsider.com/careers/quality-assurance/'
        self.driver.get(qa_url)
        # self.wait.until(ec.url_changes(qa_url))
        return QaPage(self.driver)

  


    

    # def finalize(self):
    #     if self.errors:
    #         error_message = "\n".join(self.errors)
    #         raise AssertionError(f"Soft assertion failed with the following messages: {error_message}")

    # def take_screenshot(self, test_status):
    #     filename = f"test_result_{test_status}.png"
    #     self.driver.save_screenshot(filename)

    # def menu_click(self,name):
    #     elements = self.driver.find_elements(self.menu)
    #     [i for i in elements if i.text=='Company'][0].click()
    
    # def dropdown_click(self,name):
    #     elements = self.driver.find_elements(self.dropdown_menu)
    #     [i for i in elements if i.text=='Careers'][0].click()
    #     return career_page(self.driver)

        


