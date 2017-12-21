'''
Created on Nov 23, 2017

@author: tarun.walia
'''
import unittest
from com.flipkart.utilfactory.ReadPropertyFile import ReadPropertyFile
from selenium.webdriver.common.by import By
from com.flipkart.pages.LoginPage import LoginPage

class LoginTest(unittest.TestCase):
    readFile = ReadPropertyFile()
    loginPage=LoginPage()  
    
    def test_InvalidLogin(self):
        prop=self.readFile.readPropertyFile()
        self.loginPage.navigateToURL(prop["url"])
        self.loginPage.find_element(By.CLASS_NAME, LoginPage.USER_NAME, "SENDKEYS", "9999009989")
        self.loginPage.find_element(By.XPATH, LoginPage.PASSWORD, "SENDKEYS", "testPass")
        self.loginPage.find_element(By.XPATH, LoginPage.LOGIN, "CLICK")
    
    @classmethod    
    def tearDown(self):
        self.loginPage.tearDown() 
        
        