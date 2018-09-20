from selenium import webdriver
#from selenium.webdriver.common.by import By
from pages.home.login_screen import LoginPage
import unittest
import pytest




class LoginTests(unittest.TestCase):
    baseURL = "http://192.168.1.120/LISQA/App/CareDataApp/Framework/Views/login.html"
    driver=webdriver
    driver = driver.Chrome("E:\Caredata\chrome driver\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(baseURL)
    lp=LoginPage(driver)
    
   
        
    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("amarnath", "qa@123")
        result = self.lp.verifyLoginFailed()
        print("Faild")
        assert result == True
        
    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.clickalertbtn()
    # 
        self. lp.login("qaamarnath", "qa@123")
        result = self.lp.verifyLoginSuccessful()
        assert result == True
        print("sucess")
        self.driver.quit()
        
      
       
       
       
        
        
        
        
        
        

       
    
    