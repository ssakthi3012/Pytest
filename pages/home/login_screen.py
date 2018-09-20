      
from base.selenium_driver import SeleniumDriver
import Utilites.Custome_logg as cl
import logging

class LoginPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    
    _email_field = "first_name"
    _password_field = "email"
    _login_button = ".//*[@id='contact_form']/fieldset/div/div[3]/div/p/button[1]"
    _worngusername_btn ="txtalert"

    # def getLoginLink(self):
    #     return self.driver.find_element(By.LINK_TEXT, self._login_link)
    #
    # def getEmailField(self):
    #     return self.driver.find_element(By.ID, self._email_field)
    #
    # def getPasswordField(self):
    #     return self.driver.find_element(By.ID, self._password_field)
    #
    # def getLoginButton(self):
    #     return self.driver.find_element(By.NAME, self._login_button)

    #def clickLoginLink(self):
        #self.elementClick(self._login_link, locatorType="link")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field,locatorType="name")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field,locatorType="name")

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")
        
    def clickalertbtn(self):
        self.elementClick(self._worngusername_btn, locatorType="id")

    def login(self, email, password):
        self.enterEmail(email)
        self.enterPassword(password)
        self.clearFields()
        self.clickalertbtn()
        self.clickLoginButton()    
       
    def verifyLoginSuccessful(self):
        result=self.isElementPresent("//select[@ng-model='ObjRegistration.Demographics.Title']", locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result=self.isElementPresent(".//div[@id='modernAlert']//p[contains(text(),'Your username or password is incorrect')]", locatorType="xpath")
        return result
    
    def clearFields(self):
        usernamefield=self.getElement(locator=self. _email_field,locatorType="name")
        usernamefield.clear()
        passwordfield=self.getElement(locator=self._password_field,locatorType="name")
        passwordfield.clear()
          
             
       
    