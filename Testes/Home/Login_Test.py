from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_screen import LoginPage
import unittest
import pytest

class LoginTests(unittest.TestCase):

    def test_validLogin(self):
        baseURL = "http://192.168.1.120/LISQA/App/CareDataApp/Framework/Views/login.html"
        driver = webdriver
        driver=driver.Chrome("E:\Caredata\chrome driver\chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        lp = LoginPage(driver)
        lp.login("qadr pawan gaba", "qa@123")
        
        showtitle=lp.verifyloginsucessfully()
        assert showtitle == True
        self.driver.quit()
        
        


        #showtitle = driver.find_element(By.XPATH,"//select[@ng-model='ObjRegistration.Demographics.Title']")
        #if showtitle is not None:
           # print("Login Successful")
       # else:
            #print("Login Failed")