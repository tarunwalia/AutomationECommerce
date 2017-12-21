'''
Created on Dec 14, 2017

@author: tarun.walia
'''
from com.flipkart.pages.CommonPage import CommonPage
from selenium.webdriver.common.by import By

class HeadphonesListpage(CommonPage):
    HEADING_ELECTRONIC =(By.XPATH, '//li/a[@title="Electronics"]/span')
    MOBILE_ACCESSORIES_LIST ='//ul[@class="_2OZ78M _1fj2FQ"]/li[2]/ul[@class="QPOmNK"]'
    PAGE_HEADING_HEADPHONE= (By.XPATH, "//h1[@class='_3OA8nC']")
    HEADPHONE_TYPE=(By.XPATH, "//div[@class='_1fWl8W']/div[4]/section[@class='_2XJuDa _2Zm4Qh']")
    CHECKBOX_INTHE_EAR = "//div[@title='In the Ear']"
    FILTER_TEXT_CHECK = (By.XPATH,"//div[@class='_2bbnvJ']")
    FILTER_BLOCK=(By.XPATH, "//div[@class='_2GQLOX']/span")
    SCROLL_START_POINT =(By.XPATH, "//div[@class='_3G9WVX oVjMho']/div[@class='_3aQU3C']")
    PAGE_HEADING= "//h1[@class='_2Wy-am']"