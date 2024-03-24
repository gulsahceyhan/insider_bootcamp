from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from base.base_page import BasePage
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.keys import Keys

# from page.career_page import CareerPage

class QaPage(BasePage):
    saj = (By.CLASS_NAME,'btn.btn-outline-secondary.rounded.text-medium.mt-2.py-3.px-lg-5.w-100.w-md-50')
    filter_by_loc = (By.ID,'filter-by-location')
    filter_by_dep = (By.ID,'filter-by-department')
    jobs = (By.CLASS_NAME,'position-list-item-wrapper.bg-light')
    position = (By.CLASS_NAME,'position-title.font-weight-bold')
    department = (By.CLASS_NAME,'position-department.text-large.font-weight-600.text-primary')
    location = (By.CLASS_NAME,'position-location.text-large')
    view_role = (By.CLASS_NAME,'btn.btn-navy.rounded.pt-2.pr-5.pb-2.pl-5')
    

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_page_load()
    
    def wait_page_load(self):
        self.wait.until(ec.visibility_of_element_located(self.saj))
    
    def saj_click(self):
        self.driver.find_element(*self.saj).click()
        # self.driver.execute_script("arguments[0].click();", saj)
        body = self.driver.find_element(By.TAG_NAME,'body')
        body.send_keys(Keys.PAGE_DOWN)
        self.wait.until(ec.visibility_of_element_located(self.filter_by_loc))
    
    def filter(self):
        dep = Select(self.driver.find_element(*self.filter_by_dep)) 
        loc = Select(self.driver.find_element(*self.filter_by_loc)) 
        time.sleep(5)
        dep.select_by_visible_text('Quality Assurance')
        loc.select_by_visible_text('Istanbul, Turkey')
        time.sleep(2)
    
    def suitable_jobs(self):
        self.wait.until(ec.presence_of_all_elements_located(self.jobs))
        jobs = self.driver.find_elements(*self.jobs)

        for job in jobs:
            try:
                position = job.find_element(*self.position).text
                department = job.find_element(*self.department).text
                location = job.find_element(*self.location).text
            except Exception as e:
                print(e)

            if ('Quality Assurance' in position) and ('Quality Assurance' in department) and ('Istanbul, Turkey' in location):
                print('suitable')
            else:
                print(f'{position}-{department}-{location} not suitable')
    
    def navigate_lever_app(self):
        #GO JOB FORM
        view_role = self.driver.find_element(*self.view_role)
        self.driver.execute_script("arguments[0].click();", view_role)

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        if self.driver.current_url =='https://jobs.lever.co/useinsider/78ddbec0-16bf-4eab-b5a6-04facb993ddc':
            print('Lever Application opened.')
        else:
            print("Cound't open")
    
    def exit_driver(self):
        self.driver.quit()

    
   
        # return CareerPage(self.driver)

        


