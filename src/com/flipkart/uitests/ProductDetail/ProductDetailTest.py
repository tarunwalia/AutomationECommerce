'''
Created on Nov 30, 2017

@author: tarun.walia
'''
import unittest
from com.flipkart.pages.CommonPage import CommonPage
from com.flipkart.utilfactory.ReadPropertyFile import ReadPropertyFile
from selenium.webdriver.common.by import By
from com.flipkart.pages.ProductDetailPage import ProductDetailPage
import time

class ProductDetailTest(unittest.TestCase):
    prop = ReadPropertyFile()
    prop=prop.readPropertyFile()
    productDetail= ProductDetailPage()
    
    def test_validate_product_listPage(self):
        self.productDetail.navigateToURL(self.prop["url"])
#         self.commonPage.login(self.prop["username"], self.prop["password"])
        self.productDetail.find_element(By.XPATH, self.productDetail.CROSS_ICON, "CLICK")
        self.productDetail.find_element(By.XPATH, self.productDetail.SEARCH_BOX, "SENDKEYS", "shoes")
        time.sleep(2)
        items = self.productDetail.getElementsList(self.productDetail.SEARCH_TEXT_BOX)
        for item in items:
            text= item.text
            if text == "shoes men":
                self.productDetail.driver.find_element_by_link_text(text).click()
        
        time.sleep(3)        
        text = self.productDetail.getElementText(By.XPATH, self.productDetail.SHOES_LISTPAGE_HEADING)    
        data = text.split("for \"")
        text= data[1][:-1]
        self.assertEquals(text, "shoes men", text+" is not matching to shoes men.")
        
        
#     def test_validate_nikeShoes(self):
#             self.productDetail.click_brand_checkbox(By.XPATH, self.productDetail.BRAND_NIKE_CHECKBOX)
#             items=self.productDetail.get_element_list(By.XPATH, self.productDetail.PRODUCT_NAME)
#             for item in items:
#                 print item.text
    
    @classmethod
    def tearDown(self):
        self.productDetail.tearDown()
        
    