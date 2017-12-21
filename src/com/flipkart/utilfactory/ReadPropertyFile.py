'''
Created on Nov 23, 2017

@author: tarun.walia
'''

import ConfigParser
class ReadPropertyFile():
    
    def readPropertyFile(self):
        config = ConfigParser.ConfigParser()
        config.read("D:/PWorkSpace1/AutomationECommerce/Environment.properties")
        prop = dict(config.items("Env_Variables"))
        return prop
