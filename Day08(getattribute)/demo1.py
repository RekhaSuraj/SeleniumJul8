from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("file:///F:/Rekha/GRKTrainings/SeleniumJul8/Pages/sample2.html")
time.sleep(2)

print(driver.find_element(By.ID,"a1").get_attribute('name'))
# n1

print(driver.find_element(By.ID,"a1").get_attribute('class'))
# c1

print(driver.find_element(By.ID,"a1").get_attribute('href'))
# http://gmail.com/

print(driver.find_element(By.ID,"a1").get_attribute('text'))
# Click Here

