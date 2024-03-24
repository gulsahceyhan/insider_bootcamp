import unittest 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class BaseTest(unittest.TestCase):
    driver = 'chrome'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.driver = self.get_driver(self.driver)
        self.driver.get('https://useinsider.com/')
        self.driver.maximize_window()
    
    def get_driver(self, driver):
        chr_options = Options()
        chr_options.add_experimental_option("detach", True)
        chr_options.add_argument("--disable-notifications") 
        chr_options.add_argument("--disable-cookies")

        if driver == 'chrome':
            self.driver = webdriver.Chrome(options=chr_options)
        elif driver == 'safari':
            self.driver = webdriver.Safari()
        elif driver == 'firefox':
            self.driver = webdriver.Firefox()
        return self.driver