'''
Created on Dec 19, 2017

@author: tarun.walia
'''
from com.flipkart.pages.ProductDetailPage import ProductDetailPage
import unittest
import time
from com.flipkart.utilfactory.ReadPropertyFile import ReadPropertyFile
from selenium.webdriver.common.by import By
class Headset_ProductDetail(unittest.TestCase):
    prop = ReadPropertyFile().readPropertyFile()
    product_detail_page =ProductDetailPage()    
    
    def test_product_price_details(self):
        self.product_detail_page.navigateToURL(self.prop.get("url", "http://tarun.com"))
        self.product_detail_page.find_element(By.XPATH, self.product_detail_page.CROSS_ICON, "CLICK")
#         Used annotation page factory model for navigating to element
        self.product_detail_page.driver.find_element(*ProductDetailPage.HEADING_ELECTRONIC).click()
        mobile_accessories_list = self.product_detail_page.getElementsList(self.product_detail_page.MOBILE_ACCESSORIES_LIST)
        for item in mobile_accessories_list:
            text = item.text
            if text == "Headphones & Headsets":
                self.product_detail_page.driver.find_element_by_link_text(text).click()
        time.sleep(4)  
        ele = self.product_detail_page.driver.find_element(*ProductDetailPage.HEADPHONE_TYPE)
        loc = ele.location_once_scrolled_into_view
        ele.click()
        self.product_detail_page.find_element(By.XPATH, self.product_detail_page.CHECKBOX_INTHE_EAR, "CLICK")
        time.sleep(3)
#         getting the amount
        amount_on_list_page=self.product_detail_page.get_element_with_Xpath_looping(By.XPATH, self.product_detail_page.CURRENT_AMOUNT)
        time.sleep(3)
        
        
        product_name =self.product_detail_page.getElementText(By.XPATH, self.product_detail_page.PRODUCT_NAME)
        print product_name
        if "Headset" in product_name:
            self.product_detail_page.driver.find_element_by_link_text(product_name).click()
        
        time.sleep(4)    
        amount_on_detail_page=self.product_detail_page.get_element_with_Xpath_looping(By.XPATH, self.product_detail_page.CURRENT_AMOUNT)
        
        arr_list = amount_on_list_page.split("-")
        current_amount_list_page=  arr_list[0]
        actual_amount_list_page = arr_list[1]
        discount_list_page = arr_list[2]
        
        print discount_list_page
        
        
        
        
            
        
              
        
        
    