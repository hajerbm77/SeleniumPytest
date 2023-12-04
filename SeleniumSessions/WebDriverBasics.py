import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("http://www.google.com")

driver.find_element(By.NAME,'q').send_keys("naveen automationlabs")
options = driver.find_elements(By.TAG_NAME,"div.matches cr-realbox-match")
print(len(options))

for ele in options:
     # print(ele.text)
    if ele.text == 'naveen automationLabs youtube':
        ele.click()
        break

print(driver.title)
time.sleep(5)
driver.quit()