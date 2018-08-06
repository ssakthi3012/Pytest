'''
Created on 19-Mar-2018

@author: sakthi.be
'''
from selenium import  webdriver
from selenium.webdriver.common.by import By
from Pages.Home.Loginpage import Homepage
import unittest
#from selenium.webdriver.chrome import webdriver
        

class Loginpage(unittest.TestCase):
    def test_Login(self):
        Url="http://automationpractice.com/"
        #system.setProperty("webdriver.chrome.driver", ".//Driver//Chrome//chromedriver_win32//chromedriver.exe")
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(2)
        driver.get(Url)
        
        lp=Homepage(driver)
        lp.login("sakthi301289@gmail.com","abcdefg")
        
        page=driver.find_element(By.XPATH,"html/body/div[1]/div[1]/header/div[2]/div/div/nav/div[1]/a/span")
        if page is not None:
            print ("ok")
        else:
            print("try")
