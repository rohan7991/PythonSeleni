import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.w3schools.com/')

driver.find_element(By.ID,'navbtn_tutorials').click()
driver.find_element(By.ID, 'filter-tutorials-input').send_keys("Java")
driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/nav[1]/div[1]/div/div[4]/div[1]/div[5]/a[2]').click()


time.sleep(10)
driver.quit()