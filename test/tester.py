import sys
sys.path.insert(0, 'C:/Users/New/OneDrive/bootcamp')
from base.base_test import BaseTest
from page.home_page import HomePage




class TestPom(BaseTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_pom()
    # driver = 'chrome'
    def test_pom(self):
        home = HomePage(self.driver)
        home.close_cookies()
        home.menu_click('Company')
        career = home.dropdown_click('Careers')
        career.life_insider_loaded()
        career.teams_loaded()
        career.locations_loaded()
        qa = career.qa_page()
        qa.saj_click()
        qa.filter()
        qa.suitable_jobs()
        qa.navigate_lever_app()
        qa.exit_driver()
        
TestPom()