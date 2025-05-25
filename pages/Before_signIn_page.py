import time
from selenium.webdriver.common.by import By
from time import sleep
from configs.properties import Properties
# from commons import lib_global.py

class Before_signIn:
    """This class consists of automated tests of Login Page"""
    def launchURL(driver):
        driver.get(Properties.url)
        time.sleep(5)