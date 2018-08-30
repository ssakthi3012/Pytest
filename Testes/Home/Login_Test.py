
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_screen import LoginPage
#from Utilites.Constant import Constant
import unittest


class LoginTestes(unittest.TestCase):
    
    def test_validLogin(self):
       
        urladdress="http://192.168.1.120/LISQA/App/CareDataApp/Framework/Views/login.html"
        driver=webdriver
        driver=driver.Chrome("E:\Chrome\chromedriver_win32\chromedriver.exe")
        driver.implicitly_wait(2)
        driver.get(urladdress)
        driver.implicitly_wait(2)
        lp=LoginPage(driver)
        #driver.implicitly_wait(2)
        lp.login("qakarthi", "qa@123")
        
        showtitle=driver.find_element(By.XPATH,"//select[@ng-model='ObjRegistration.Demographics.Title']")
        
        if showtitle is not None:
            print "sucess"
        else:
            print "try again"
        
        
        #username=driver.find_element_by_name("first_name")
        #username.send_keys("qadr pawan gaba")
        #passwd=driver.find_element_by_name("email")
        #passwd.send_keys("qa@123")
        #loginclick=driver.find_element_by_id(".//*[@id='contact_form']/fieldset/div/div[3]/div/p/button[1]")
        #loginclick.click()
#s=LoginTestes()
#s.test_Validlogin()