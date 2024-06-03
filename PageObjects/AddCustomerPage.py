from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class AddCustomer:

    #customer page new customers each element paths
    link_main_customer_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    link_sub_customer_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    link_add_customer_xpath = "//a[@class='btn btn-primary']"

    txt_email_xpath ="//input[@id='Email']"
    txt_pass_xpath = "//input[@id='Password']"

    txt_first_name_xpath ="//input[@id='FirstName']"
    txt_last_name_xpath ="//input[@id='LastName']"
    txt_companyname_xpath = "//input[@id='Company']"
    txt_comment_xpath = "//textarea[@id='AdminComment']"

    radio_gender_male_id = "Gender_Male"
    radio_gender_female_id = "Gender_Female"

    dob_textbox_id = "DateOfBirth"

    checkbox_tax_xpath ="//input[@id='IsTaxExempt']"
    active_account_checkbox_id = "Active"

    txt_news_xpath = "(//input[@role='searchbox'])[1]"

    list_vendor_xpath ="//select[@id='VendorId']"


    customer_roles_select_id = "SelectedCustomerRoleIds"
    listitemsofRoles_xpath = "//ul//li[@role='option']"

    saveButton_xpath = "//button[@name='save']"

    #get a driver so we can find the elements
    def __init__(self,driver):
        self.driver = driver




#Click on main menu customer
    def clickonCustomer_MainMenu(self):
        self.driver.find_element(By.XPATH,self.link_main_customer_xpath).click()
#Click on submenu of customer
    def clickonCustomer_SubMenu(self):
        self.driver.find_element(By.XPATH,self.link_sub_customer_xpath).click()
#Click on add new customer button
    def clickon_AddNewCustomer(self):
        self.driver.find_element(By.XPATH,self.link_add_customer_xpath).click()



#set email to new customer
    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txt_email_xpath).send_keys(email)
#set password to new customer
    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.txt_pass_xpath).send_keys(password)
#set FirstName to new customer info.
    def setFirstName(self,firstname):
        self.driver.find_element(By.XPATH,self.txt_first_name_xpath).send_keys(firstname)
#set Lastname to new customer info.
    def setLastName(self,lastname):
        self.driver.find_element(By.XPATH,self.txt_last_name_xpath).send_keys(lastname)
# set CompanyName to new customer info.
    def setCompanyName(self,companyname):
        self.driver.find_element(By.XPATH,self.txt_companyname_xpath).send_keys(companyname)
#set Admin Comment to new customer info.
    def setAdminComment(self,comment):
        self.driver.find_element(By.XPATH,self.txt_comment_xpath).send_keys(comment)



#set Gender into new customer info. radio button
    def setGender(self,gender):
        if gender == "Male":
            self.driver.find_element(By.ID,self.radio_gender_male_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID, self.radio_gender_female_id).click()
        else:
            self.driver.find_element(By.ID, self.radio_gender_male_id).click()




#set DOB into new customer info. date picker
    def setDOB(self,dob):
        self.driver.find_element(By.ID,self.dob_textbox_id).send_keys(dob)




#set tax exempt into new customer info. from the checkbox
    def setTaxExempt(self,value):
        checkbox = self.driver.find_element(By.XPATH, self.checkbox_tax_xpath)
        if value ==  "True":
            checkbox.click()
        else:
            pass
# set Acvtive to new customer info. from chechlbox
    def setActive(self, active):
        checkbox_element = self.driver.find_element(By.ID, self.active_account_checkbox_id)
        is_checked = checkbox_element.is_selected()
        if is_checked:
            checkbox_element.click()
        if active and not is_checked:
            checkbox_element.click()





#set News letter into new customer info. from the txtbox list
    def setNewsLetter(self,news):
        # pass
        # self.driver.find_element(By.XPATH, self.txt_news_xpath).click()
        self.driver.find_element(By.XPATH,self.txt_news_xpath).send_keys(news)



#set Customer role into to new customer info. from textbox list
    def setCustomerRole(self,role):
        list1 = self.driver.find_element(By.ID,self.customer_roles_select_id)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();",list1)
        list2 = Select(list1)
        list2.deselect_all()
        list2.select_by_visible_text(role)


#set Manager of vendor into to new customer info. from drop down list
    def setManagerofVendor(self,vendor):
        drop_down = Select(self.driver.find_element(By.XPATH,self.list_vendor_xpath))
        drop_down.select_by_visible_text(vendor)




#click on save button
    def clickOnSave(self):
        self.driver.find_element(By.XPATH,self.saveButton_xpath).click()


