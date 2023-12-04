from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.amazon.com')
print(driver.title)

links = driver.find_elements(By.TAG_NAME, 'a')
print(len(links))

for link in links:
    if link.text == 'Holiday Deals':
        print(link.get_attribute('href'))
        link.click()
        break

imageList = driver.find_elements(By.TAG_NAME, 'img')
print(len(imageList))

for image in imageList:
    print(image.get_attribute('scr'))



driver.quit()