import time

import pytest
from selenium import webdriver
from PageObjects.Login import Login
from Utilities.readProperties import ReadConfig
from Utilities.cutomLogger import LogGen
from PageObjects.CustomerRolesPage import  CustomerRolesPage

class Test_Case_004_Customer_Roles:

    baseURL = ReadConfig.getApplicationURL()#get the url
    username = ReadConfig.getUsername()#get the username
    password = ReadConfig.getPassword()#get the password

    logger = LogGen.loggen()#get log class object to add log

    #to loging
    def test_Login(self, setup):
        self.logger.info("***********Test case 003 Add Customer ********************")
        self.driver = setup  # to get a driver from setup-->confest.py-->TestCases
        self.driver.get(
            self.baseURL)  # get the URL from method getApplicationURL-->ReadConfig-->readProperties-->Utilities
        self.driver.maximize_window()

        # create Login.py-->PageObjects page object to find element and pass the data
        self.login_object = Login(self.driver)
        self.login_object.set_username(self.username)  # get the username from ReadConfig and pass in to login page
        self.login_object.set_password(self.password)
        self.login_object.click_login()

        self.logger.info("***************Login Successful****************")

        self.logger.info("Test case of edit role begin")
        self.customerroleedit_obj = CustomerRolesPage(self.driver)
        self.customerroleedit_obj.clickonCustomer_MainMenu()
        self.customerroleedit_obj.clickonCustomerRoles()
        self.customerroleedit_obj.clickonEdit("Administrators")

        time.sleep(10)
        self.driver.close()








