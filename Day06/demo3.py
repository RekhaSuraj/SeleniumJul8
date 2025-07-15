from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("https://opensource-demo.orangehrmlive.com")
time.sleep(3)

un_loc = driver.find_element(By.XPATH,"//input[@placeholder='Username']").location
print(un_loc)
print(un_loc['x'])

pwd_loc = driver.find_element(By.XPATH,"//input[@type='password']").location
print(pwd_loc)
print(pwd_loc['x'])

if un_loc['x'] == pwd_loc['x']:
    print('UN and Pwd are aligned')

else:
    print('UN and Pwd are not aligned')