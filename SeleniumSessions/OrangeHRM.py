from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.orangehrm.com/orangehrm-30-day-trial')
print(driver.title)
driver.find_element(By.ID, 'Form_getForm_subdomain').send_keys('tester123')
driver.find_element(By.ID, 'Form_getForm_Name').send_keys('tester')
driver.find_element(By.ID, 'Form_getForm_Email').send_keys('tester123@gmail.com')
driver.find_element(By.ID, 'Form_getForm_Contact').send_keys('7028876677')

driver.quit()