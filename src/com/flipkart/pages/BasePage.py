'''
Created on Nov 23, 2017

@author: tarun.walia
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

class BasePage():
    def __init__(self):
#         webdriver.Chrome()
        chromeDriver = "D:/PWorkSpace1/AutomationECommerce/geckodriver/chromedriver.exe"
        self.driver = webdriver.Chrome(chromeDriver)
        
    
    def tearDown(self):
        self.driver.quit()    
          
        