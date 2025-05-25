from selenium.webdriver.common.by import By
import time
from commons import lib_global
class login_with_invalid_cred:
    def click_SignIn(driver):
        print("1")
        driver.implicitly_wait(20)
        lib_global.click_element(driver, "xpath", "//span[text()='Sign In']")
        pass
    def send_username_and_password(driver, username, password):
        lib_global.send_keys(driver, "xpath", "//input[@placeholder='Username or E-mail']", username)
        lib_global.send_keys(driver, "xpath", "//input[@placeholder='Password']", password)
        lib_global.click_element(driver, "xpath", "//span[text()='Sign In']")