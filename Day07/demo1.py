from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("https://opensource-demo.orangehrmlive.com")
time.sleep(2)

un_size = driver.find_element(By.XPATH,"//input[@name='username']").size
print(un_size)
un_h = un_size['height']
un_w = un_size['width']

pwd_size = driver.find_element(By.XPATH,"//input[@name='password']").size
print(pwd_size)
pwd_h = pwd_size['height']
pwd_w = pwd_size['width']

time.sleep(3)

if un_h == pwd_h:
    print('Height is aligned')
else:
    print('Height is not aligned')


if un_w == pwd_w:
    print('width is aligned')
else:
    print('width is not aligned')


# {'height': 45, 'width': 300}
# {'height': 45, 'width': 300}

# Height is aligned
# width is aligned