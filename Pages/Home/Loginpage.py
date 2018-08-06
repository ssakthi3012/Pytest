'''
Created on 19-Mar-2018

@author: sakthi.be
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

class Homepage():
    def __init__(self,driver):
        self.driver=driver
        #Locator
        _login_link="html/body/div[1]/div[1]/header/div[2]/div/div/nav/div[1]/a"
        _username_link="email"
        _password_link="passwd"
        _singin_link="SubmitLogin"
        
        def getloginlink(self):
            return self.driver.find_element(By.XPATH,_login_link)
        def getusernamefield(self,username):
            return self.driver.find_element(By.ID,_username_link)
        def getpasswordfield(self,password):
            return self.driver.find_element(By.ID,_password_link)
        def clicksinginbtn(self):
            return self.driver.find_element(By.ID,_singin_link)
        def loginlink(self):
            self.getloginlink().click()
        def username(self):
            self.getusernamefield().send_keys()
        def pswrd(self):
            self.getpasswordfield().send_keys()
        def signbtn(self):
            self.clicksiginbtn().click()
            
        def login(self,username,password):
            self.loginlink()
            self.username()
            self.pswrd()
            self.signbtn()