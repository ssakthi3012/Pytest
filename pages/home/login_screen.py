
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDrivers


class LoginPage(SeleniumDrivers):
    
    def __init__(self, driver):
       # super().__init__(driver)
        self.driver=driver
        
    #Locators
    _login_name="first_name"
    _login_pswd="email"
    _signin=".//*[@id='contact_form']/fieldset/div/div[3]/div/p/button[1]"
    
    #Find elements
    #def getUsrname(self):
        #return self.driver.find_element(By.NAME,self._login_name)
    #def getpasswd(self):
        #return self.driver.find_element(By.NAME,self._login_pswd)
    #def loginclick(self):
        #return self.driver.find_element(By.XPATH,self._signin)
    
    #def enterusername(self,username):
        #self.getUsrname().send_keys(username)
    #def enterpassword(self,password):
        #self.getpasswd().send_keys(password)
    #def loginbutton(self):
        #self.loginclick().click()
      
    #send keys
    def enterusername(self, username):
        self.sendkeys(username,self._login_name)
    def enterpassword(self, password):
        self.sendkeys(password,self._login_pswd)
        
    #Click login
    def loginbutton(self):
        self.elementClick(self._signin,locatorType="xpath")
        
    #Login fuction       
    def login(self, username, password):
        self.enterusername(username)
        self.enterpassword(password)
        self.loginbutton()
        
        
          
             
       
    