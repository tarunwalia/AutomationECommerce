'''
Created on Dec 14, 2017

@author: tarun.walia
'''
import unittest
from com.flipkart.pages.HeadphonesListPage import HeadphonesListpage
from com.flipkart.utilfactory.ReadPropertyFile import ReadPropertyFile
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
class HeadphonesListTest(unittest.TestCase):
    checkPage=False
    head_phone_list_page= HeadphonesListpage()
    prop = ReadPropertyFile()
    prop = prop.readPropertyFile()
    
    def test_headphoneList_page(self):
        self.head_phone_list_page.navigateToURL(self.prop.get("url", "http://www.tarun.com"))
        self.head_phone_list_page.find_element(By.XPATH, self.head_phone_list_page.CROSS_ICON, "CLICK")
#         Used annotation page factory model for navigating to element
        self.head_phone_list_page.driver.find_element(*HeadphonesListpage.HEADING_ELECTRONIC).click()
        
        mobile_accessories_list = self.head_phone_list_page.getElementsList(self.head_phone_list_page.MOBILE_ACCESSORIES_LIST)
        for item in mobile_accessories_list:
            text = item.text
            if text == "Headphones & Headsets":
                self.head_phone_list_page.driver.find_element_by_link_text(text).click()
        time.sleep(2)        
        page_heading=self.head_phone_list_page.driver.find_element(*HeadphonesListpage.PAGE_HEADING_HEADPHONE).text
        time.sleep(2)
        self.assertEqual("Headphones", page_heading, "Page heading is not matching for Headphone & Headset page.")
        
    
    @unittest.skipIf(False, "test_headphoneList_page testcase failed during execution so skipping.")
    def test_headphone_type_filter(self):
        ele = self.head_phone_list_page.driver.find_element(*HeadphonesListpage.HEADPHONE_TYPE)
#         get location and scroll up to the element
        loc = ele.location_once_scrolled_into_view
#         Scroll up to the element with Action class
#         action = ActionChains(self.head_phone_list_page.driver)
#         action.move_to_element(ele).perform()
        ele.click()
        self.head_phone_list_page.find_element(By.XPATH, self.head_phone_list_page.CHECKBOX_INTHE_EAR, "CLICK")
        time.sleep(3)
#         verify the filter section
        filter_block_text = self.head_phone_list_page.driver.find_element(*HeadphonesListpage.FILTER_BLOCK).text
        self.assertEquals("Filters", filter_block_text, "Filters block is not visible.")
        filter_text = self.head_phone_list_page.driver.find_element(*HeadphonesListpage.FILTER_TEXT_CHECK).text
        self.assertEqual("In the Ear", filter_text, "Applied filter text is not matching.")
        
#         scroll with ActionChan class
        scroll_ele =self.head_phone_list_page.driver.find_element(*HeadphonesListpage.SCROLL_START_POINT)
        action_scroll = ActionChains(self.head_phone_list_page.driver)
        action_scroll.click_and_hold(scroll_ele).move_by_offset(30, 0).perform()
        time.sleep(4)
        self.head_phone_list_page.web_driver_wait(8, self.head_phone_list_page.PAGE_HEADING)
        
        
                
            