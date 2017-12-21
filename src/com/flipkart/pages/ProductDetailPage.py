'''
Created on Nov 30, 2017

@author: tarun.walia
'''
from com.flipkart.pages.CommonPage import CommonPage
from selenium.webdriver.common.by import By
class ProductDetailPage(CommonPage):
    SEARCH_BOX="//input[@name='q']"
    SEARCH_TEXT_BOX= "//ul[@data-reactid='52']"
    SHOES_LISTPAGE_HEADING="//div[@class='KG9X1F']/h1/span"
    BRAND_NIKE_CHECKBOX="//div[@class='_4IiNRh _-9cJSB' and @title='Nike']"
    PRODUCT_NAME = "//a[@class='_2cLu-l']"
    HEADING_ELECTRONIC =(By.XPATH, '//li/a[@title="Electronics"]/span')
    PAGE_HEADING_HEADPHONE= (By.XPATH, "//h1[@class='_3OA8nC']")
    MOBILE_ACCESSORIES_LIST ='//ul[@class="_2OZ78M _1fj2FQ"]/li[2]/ul[@class="QPOmNK"]'
    HEADPHONE_TYPE=(By.XPATH, "//div[@class='_1fWl8W']/div[4]/section[@class='_2XJuDa _2Zm4Qh']")
    CHECKBOX_INTHE_EAR = "//div[@title='In the Ear']"
    PRODUCT_NAME ="//div[@class='_3liAhj']/a[@class='_2cLu-l']"
    CURRENT_AMOUNT="//div[@class='_1uv9Cb']/div["
        
    def click_brand_checkbox(self, identifier, ele_attr):
        ele=self.driver.find_element(identifier, value=ele_attr)
        val=ele.click()        
    
    def get_element_list(self, identifier, ele_attr):
        items= self.driver.find_elements(identifier, value=ele_attr)
        return items