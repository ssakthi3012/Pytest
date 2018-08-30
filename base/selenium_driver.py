'''
Created on Aug 29, 2018

@author: CD001
'''

from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.common.exceptions import *
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementNotSelectableException

class SeleniumDrivers():
    def __init__ (self,driver):
        self.driver=driver
        
    def getByType(self,loctorType):
        locatorType=loctorType.lower()
        if locatorType =="id":
            return By.ID
        elif locatorType =="name":
            return By.NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "xpath":
            return By.XPATH
        else:
            print("Loctaor Type:"+ locatorType+"not supported")
            return False
    def getElement(self,locator,locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element =self.driver.find_element(byType, locator)
            print("Element found")
        except:
            print("Element not found")
        return element
    def ElementClick(self,locator,locatorType="id"):
        try:
            element=self.driver.find_element(locator,locatorType)
            element.click()
            print("Element Clicke with locator" + locator + "locatorType:" + locatorType)
        except:
            print("Element cann't clickable")
            print_stack()  
            
    def sendkeys(self,Data,locator,locatorType="id"):
        try:
            element=self.driver.find_element(locator,locatorType)
            element.send_keys(Data)   
            print("Elent send data"+locator+"locator Type:"+locatorType)
        except:
            print("cann't send data")
            print_stack()
            
    def isElementPresent(self,locator,locatorType="id"):
        try:
            element =self.getElement(locator, locatorType)
            if element is not None:
                print("Element Found")
                return True
            else:
                print("Element is not Found")
                return False
        except:
            print("Element is not Found")
            return False
    def isElementtpresencecheck(self,locator,byType):
        try:
            elementlist = self.driver.find_elements(byType,locator)
            if len(elementlist)  > 0:
                print("Elements is found")
                return True
            else:
                print("Elements is not found")
                return False
        except:
            print("Element is not foud")
            return False
    def waitForElement(self,locator,locatorType="id",timeout=10,pollFrequence=0.5):
        element = None
        try:
            byType =self.getByType(locatorType)
            print("waiting max.time::" + str(timeout) + "::seconds for elemints for clickable")
            wait=WebDriverWait(self.driver, 10, poll_frequency=1,
                              ignored_exceptions=NoSuchElementException,
                               ElementNotVisibleException,ElementNotSelectableException)
            
            element=wait.until(Ec.element_to_be_clickable(byType,"stopFilter_stops-0"))
            print("Element appeared on the page")
        except:
            print("Element not appeared on the page")
            print_stack()
        return False
            
    
                
        
            
        
    