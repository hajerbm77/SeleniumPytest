from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https:classic.crmpro.com/')
print(driver.title)

driver.quit()
