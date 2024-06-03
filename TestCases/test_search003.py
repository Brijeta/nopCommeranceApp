import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from PageObjects.Login_AdminPageObject import Login
from PageObjects.AddCustomerPage import AddCustomer
from Utilities.readProperties import ReadConfig
from Utilities.cutomLogger import LogGen
from selenium.webdriver.common.by import By
from PageObjects.CustomerRolesPage import CustomerRolesPage
from PageObjects.SearchCustomer import SearchCustomer


class Test_searchCustomerByname_004:
    #get the basic information forn config file to login
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    #generate logs
    logger = LogGen.loggen()

    
    def test_SearchCustomerByname(self,setup):
        self.logger.info("***********Test case 004 search Customer By name ********************")
        self.driver = setup #to get a driver from setup-->confest.py-->TestCases
        self.driver.get(self.baseURL) #get the URL from method getApplicationURL-->ReadConfig-->readProperties-->Utilities
        self.driver.maximize_window()

        #create Login.py-->PageObjects page object to find element and pass the data
        self.login_object = Login(self.driver)
        self.login_object.set_username(self.username) #get the username from ReadConfig and pass in to login page
        self.login_object.set_password(self.password)
        self.login_object.click_login()

        self.logger.info("***************Login Successful****************")
        self.logger.info("Search the customer by name test case begin")

        self.customer_click = AddCustomer(self.driver)
        self.customer_click.clickonCustomer_MainMenu()
        time.sleep(2)
        self.customer_click.clickonCustomer_SubMenu()
        self.search_customer = SearchCustomer(self.driver)

        self.search_customer.setFirstname("Virat")
        self.search_customer.clickOnsearchButton()
        self.logger.info("Search by name 'Virat'")
        time.sleep(2)
        self.logger.info("Test Case Ended")

        self.driver.close()

