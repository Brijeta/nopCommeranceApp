import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import pytest

class CustomerRolesPage:

    def __init__(self,driver):
        self.driver = driver

    def clickonCustomer_MainMenu(self):
        self.driver.find_element(By.XPATH,"//a[@href='#']//p[contains(text(),'Customers')]").click()

    def clickonCustomerRoles(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//a[@href='/Admin/CustomerRole/List']").click()

    def clickonEdit(self,role):
        time.sleep(2)
        self.Listofroles  = self.driver.find_elements(By.XPATH,"//*[@id='customerroles-grid']/tbody/tr/td")
        count = 0
        for r in self.Listofroles:
            count = 1
            if r.text == role:
                self.ele = self.driver.find_element(By.XPATH,"//a[@href='Edit/"+str(count)+"']")
                time.sleep(2)
                count +=1
                # print("\n\n if inside loop values: ", count,"\n\n", r.text)
        self.ele.click()
    time.sleep(2)

