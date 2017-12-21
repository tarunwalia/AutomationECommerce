'''
Created on Nov 24, 2017

@author: tarun.walia
'''
from selenium.webdriver.common.by import By
from com.flipkart.pages.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

class CommonPage(BasePage):
    USER_NAME = "_2zrpKA"
    PASSWORD = "//*[@class='_2zrpKA _3v41xv']"
    LOGIN = "//*[@class='_2AkmmA _1LctnI _7UHT_c']"
    CROSS_ICON="//button[@class='_2AkmmA _29YdH8']"
    
        
    def navigateToURL(self, url):
        self.driver.get(url)  

    def login(self, userName, password):
        self.find_element(By.CLASS_NAME, self.USER_NAME, "SENDKEYS",userName)
        self.find_element(By.XPATH, self.PASSWORD, "SENDKEYS",password)
        self.find_element(By.XPATH, self.LOGIN, "CLICK")
        
    def find_element(self, identifier, ele_attr, operation, value1=None):
        if (operation == 'CLICK'):
            self.driver.find_element(identifier, value=ele_attr).click();
        if (operation == 'SENDKEYS'):
            self.driver.find_element(identifier, value=ele_attr).send_keys(value1);
            
    
    def getElementText(self, identifier, ele_attr):
        text= self.driver.find_element(identifier, value=ele_attr).text
        return text
        
    
    def click_checkbox(self, identifier, ele_attr):
        ele=self.driver.find_element(identifier, value=ele_attr)
        ele.click()
        isChecked =ele.selected
        return isChecked  
        
    def getElementsList(self, identifier):
        html_list=self.driver.find_element(By.XPATH, value=identifier)
        items = html_list.find_elements_by_tag_name("li")
        return items  
    
    def web_driver_wait(self, timeslot, element):
        try:
            text=self.driver.find_element(By.XPATH, element).text
            wait = WebDriverWait(self.driver, timeslot)
            wait.until(expected_conditions.text_to_be_present_in_element((By.XPATH, element),text), timeslot)
        except TimeoutException, e:
            e.message 
            
    def get_element_with_Xpath_looping(self,identifier, element):
        text1=""
        for i in range(1,4):
            ele = element+str(i)+"]"
            text=self.driver.find_element(identifier, value=ele).text.replace(u"\u20B9","")
            text1 += text+"-"
        return text1[:-1]  
                
            
                  