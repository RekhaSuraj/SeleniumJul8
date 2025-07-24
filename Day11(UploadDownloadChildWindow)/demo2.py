# We can also specify path in a variable using os import
import os
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

driver = Chrome()
driver.get('file:///F:/Rekha/Rekha/BhanuClasses/Selenium/Pages/sample13.html')
time.sleep(2)
path1 = os.path.abspath("TestUpload.txt")
print(path1)
# For upload - we have to send the filepath in send_keys of the element
driver.find_element(By.ID,'A2').send_keys(path1)

time.sleep(4)



