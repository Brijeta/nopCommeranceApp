import random
import time
import pytest
import string
from selenium import webdriver
from PageObjects.Login import Login
from PageObjects.AddCustomerPage import AddCustomer
from Utilities.readProperties import ReadConfig
from Utilities.cutomLogger import LogGen
from selenium.webdriver.common.by import By

class Test_003_Add_customer_TestCase:

    #get the basic information forn config file to login
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    #generate logs
    logger = LogGen.loggen()


    def test_addCustomer(self,setup):
        self.logger.info("***********Test case 003 Add Customer ********************")
        self.driver = setup #to get a driver from setup-->confest.py-->TestCases
        self.driver.get(self.baseURL) #get the URL from method getApplicationURL-->ReadConfig-->readProperties-->Utilities
        self.driver.maximize_window()

        #create Login.py-->PageObjects page object to find element and pass the data
        self.login_object = Login(self.driver)
        self.login_object.set_username(self.username) #get the username from ReadConfig and pass in to login page
        self.login_object.set_password(self.password)
        self.login_object.click_login()

        self.logger.info("***************Login Successful****************")
        self.logger.info("*************Add customer details test starting *******************")

        #create AddCustomerPage.py object to find the elements to and perform the actions
        self.addCust = AddCustomer(self.driver)

        self.addCust.clickonCustomer_MainMenu()#click on customer menu
        time.sleep(2)
        self.addCust.clickonCustomer_SubMenu()
        time.sleep(2)
        self.addCust.clickon_AddNewCustomer()
        time.sleep(2)
        self.logger.info("***********Providing Customer inforamtion **************")

        self.email = random_generator() + "@gmail.com"
        self.addCust.setEmail(self.email)
        self.addCust.setPassword("test123")
        self.addCust.setFirstName("Patel")
        self.addCust.setLastName("Pinal")
        self.addCust.setGender("Female")
        self.addCust.setDOB("03/02/2000")
        self.addCust.setCompanyName("busyB")
        self.addCust.setTaxExempt("True")
        self.addCust.setNewsLetter("Test store 2")
        self.addCust.setCustomerRole("Guests")
        self.addCust.setManagerofVendor("Vendor 2")
        self.addCust.setAdminComment("Testing Admin comment")


        self.addCust.clickOnSave()

        self.msg = self.driver.find_element(By.TAG_NAME,"body").text

        if('customer has been added successfully.' in self.msg):
            self.logger.info("**********New Cutomer data saved(Test Case paassed)********************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_addCustomer_src.png")
            self.logger.error("**********Add customer test case failed*********")

        self.addCust.clickonCustomer_SubMenu()
        time.sleep(5)
        self.driver.close()
def random_generator(size=8, chars = string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))
