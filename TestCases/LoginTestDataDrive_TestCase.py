

import pytest
from selenium import webdriver
import time
from PageObjects.Login_AdminPageObject import Login
from Utilities.readProperties import ReadConfig
from Utilities.cutomLogger import LogGen
from Utilities.xUtilite import data



class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()


    def test_Login_DDT(self,setup):
        self.logger.info("*******Test case ID 002, Data Driven test case**********")
        self.logger.info("***********Verifying Login test case **************")

        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = Login(self.driver)

        #array
        list_status =[]

        #get the data from excel sheet
        self.rows = data.get_row_count(self.path,"Sheet1")
        for r in range (2,self.rows+1):
            self.username = data.read_data(self.path,"Sheet1",r,1)
            self.password = data.read_data(self.path, "Sheet1", r, 2)
            self.value = data.read_data(self.path, "Sheet1", r, 3)

            #from excel sheet pass the data
            self.lp.set_username(self.username)
            self.lp.set_password(self.password)
            self.lp.click_login()
            time.sleep(3)

            #get title of page
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.value == "pass":
                    # self.logger.info("****Passed value from expected*****")
                    self.lp.click_logout()
                    time.sleep(3)
                    list_status.append("pass")
                elif self.value == "fail":
                    # self.logger.info("****Fail value from expected*****")
                    list_status.append("fail")

        if act_title != exp_title:
            if self.value == "pass":
                # self.logger.info("****test data from excel(correct data(Positive case) is pass but not getting into = Failed*****")
                self.lp.click_login()
                list_status.append("fail")
            elif self.value == "fail":
                # self.logger.info("****test data from excel(correct data(Negavite case) is fail should not getting into = Passed*****")
                list_status.append("pass")

        if "fail" not in list_status:
            self.logger.info("Login Data Driven Test Passed")

        else:
            self.logger.error("Login Data Driven Test Failed")
            self.logger.info("End of Login Data Driven Testing")
            self.logger.info("Completed Test_002_DDT_Login")




