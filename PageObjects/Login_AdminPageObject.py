from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import pytest

class Login:
    username_textbox_xpath = "//input[@id='Email']"
    pass_textbox_xpath ="//input[@id='Password']"
    login_button_xpath = "//button[@type='submit']"
    logout_button_xpath = "//a[normalize-space()='Logout']"

    def __init__(self,driver):
        self.driver = driver

    def set_username(self,username):
        self.driver.find_element(By.XPATH,self.username_textbox_xpath).clear()
        self.driver.find_element(By.XPATH,self.username_textbox_xpath).send_keys(username)

    def set_password(self,password):
        self.driver.find_element(By.XPATH,self.pass_textbox_xpath).clear()
        self.driver.find_element(By.XPATH,self.pass_textbox_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH,self.login_button_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH,self.logout_button_xpath).click()
