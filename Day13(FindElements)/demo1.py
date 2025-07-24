# find_elements
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

driver = Chrome()
driver.get('file:///F:/Rekha/Rekha/BhanuClasses/Selenium/Pages/sample3.html')
time.sleep(2)

# If there are multiple matching elements, find element, returns only the first matching web element
fe = driver.find_element(By.ID,'a1')
print(fe)
print(type(fe))

print(fe.get_attribute('href'))

# find_elements - Returns all the matching webelements in the form of list
fes = driver.find_elements(By.ID,'a1')
print(fes)
print(type(fes))

# <class 'list'>
print(len(fes))
# 3