# implicitly_wait
# Selenium will be faster than app and find_element will not wait.
# So we have to match selenium execution speed with the app - Synchronization
# time.sleep(10) - blind wait for 10 seconds, this is from Python

# driver.implicitly_wait(10) - wait upto 10 seconds, this is from Selenium, applicable for find_element and find_elements only
# Can handle only NoSuchElement Exception

import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get('https://opensource-demo.orangehrmlive.com')
driver.implicitly_wait(10)

driver.find_element(By.NAME,'username').send_keys('admin')
time.sleep(4)
