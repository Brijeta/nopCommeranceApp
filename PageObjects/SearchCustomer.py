from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class SearchCustomer:
    txtemail_id ="SearchEmail"
    txtfirstname_id ="SearchFirstName"
    txtlastname = "SearchLastName"
    txtcompany_id = "SearchCompany"
    txtip_id ="SearchIpAddress"
    customerrole_xpath="//ul[@class='select2-selection__rendered']"
    btnsearch_id ="search-customers"

    searchresulttable_xpath = "//table[@role='grid']"
    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customer-grid']//tbody/tr"
    tableCol_xpath = "//table[@id='customer-grid']//tbody/tr/td"

    def __init__(self,driver):
        self.driver = driver

    def setEmail(self,email):
        self.driver.find_element(By.ID,self.txtemail_id).clear()
        self.driver.find_element(By.ID, self.txtemail_id).send_keys(email)

    def setFirstname(self,firstname):
        self.driver.find_element(By.ID,self.txtfirstname_id).clear()
        self.driver.find_element(By.ID, self.txtfirstname_id).send_keys(firstname)

    def setLastname(self,lastname):
        self.driver.find_element(By.ID,self.txtlastname).clear()
        self.driver.find_element(By.ID, self.txtlastname).send_keys(lastname)

    def setCompanyID(self,companyId):
        self.driver.find_element(By.ID,self.txtcompany_id).clear()
        self.driver.find_element(By.ID, self.txtcompany_id).send_keys(companyId)

    def clickOnsearchButton(self):
        self.driver.find_element(By.ID, self.btnsearch_id).click()

    def getNoRows(self):
        return len(self.driver.find_element(By.XPATH,self.tableRows_xpath))

    def getNoCol(self):
        return len(self.driver.find_element(By.XPATH,self.tableCol_xpath))

    def searchCustomerByemail(self,email):
        flag = False
        for r in range(1, self.getNoRows()+1):
            table = self.driver.find_element(By.XPATH,self.table_xpath)
            emailid=table.find_element(By.XPATH,"//table[@id='customer-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break

        return flag

    def searchCustomerByname(self,name):
        flag = False
        for r in range(1, self.getNoRows()+1):
            table = self.driver.find_element(By.XPATH,self.table_xpath)
            names=table.find_element(By.XPATH,"//table[@id='customer-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if names == name:
                flag = True
                break

        return flag
