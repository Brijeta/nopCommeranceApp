from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
import pytest_html
from pytest_metadata.plugin import metadata_key


import pytest

@pytest.fixture
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Lunching chrome")
    elif browser == 'firefox':
        print("Lunching firefox")
        driver = webdriver.Firefox()
    elif browser=='edge':
        print("Lunching edge")
        driver = webdriver.edge()
    else:
         driver = webdriver.Chrome()
         print("Lunching chrome")
    return driver

def pytest_addoption(parser): #This will get the value from CLI/ hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #This will return the browser value to setup method
    return request.config.getoption("--browser")

#Pytest HTMl Report
def pytest_configure(config):
    metadata = config.pluginmanager.getplugin("metadata")
    if metadata:
        config.stash[metadata_key]['Project Name'] = 'nopCommerace'
        config.stash[metadata_key]['Module Name'] = 'Login Page'
        config.stash[metadata_key]['Tester'] = 'Brijeta Ghevariya'

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins", None)