from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('https://www.orangehrm.com/orangehrm-30-day-trial')
print(driver.title)


def select_values(ele, value):
    select = Select(ele)
    select.select_by_visible_text(value)


def select_values_without_Select(list, value):
    print(len(list))
    for ele in list:
        print(ele.text)
        if ele.text == value:
            ele.click()
            break

ele_country = driver.find_element(By.ID, "Form_getForm_Country")

select_values(ele_country, 'France')
# select_values_without_Select(ele_country, 'Tunisia')
# select = Select(ele_country)
# list_country = select.options
# for country in list_country:
#     print(country.text)
#     if country.text == 'France':
#         country.click()
#         break
country_list = driver.find_elements(By.XPATH, '//select[@id="Form_getForm_Country"]/option')
select_values_without_Select(country_list, "Tunisia")
# select.select_by_visible_text('Italy')
# time.sleep(7)

driver.quit()
