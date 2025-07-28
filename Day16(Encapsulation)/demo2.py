from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

driver = Chrome()
driver.get('https://opensource-demo.orangehrmlive.com')
driver.implicitly_wait(10)

a = (By.NAME,'username')
# un = driver.find_element(a[0],a[1])
un = driver.find_element(*a)
un.send_keys('admin')
time.sleep(5)