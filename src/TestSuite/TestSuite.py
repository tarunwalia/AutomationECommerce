'''
Created on Dec 7, 2017

@author: tarun.walia
'''
import os
import sys
import HTMLTestRunner
from com.flipkart.uitests.HeadphonesList.HeadphonesListTest import HeadphonesListTest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
# 
# from com.flipkart.uitests.login.LoginTest import LoginTest
# from com.flipkart.uitests.ProductDetail.ProductDetailTest import ProductDetailTest

reportDir= "D:\PWorkSpace1\AutomationECommerce\Reports"
os.path.abspath(reportDir)

# testcase_login = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
# testcase_detail = unittest.TestLoader().loadTestsFromTestCase(ProductDetailTest)
testcase_headphoneListPage = unittest.TestLoader().loadTestsFromTestCase(HeadphonesListTest)
test_suite =unittest.TestSuite([testcase_headphoneListPage])
outputFile = open(reportDir+"\Report.html", "w")

runner =HTMLTestRunner.HTMLTestRunner(stream=outputFile, title='Test Report', description='FlipKart Test cases')
runner.run(test_suite)

