# child Window

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

driver = Chrome()
driver.get('file:///F:/Rekha/Rekha/BhanuClasses/Selenium/Pages/sample13.html')
time.sleep(2)

driver.find_element(By.ID,'A5').click()
time.sleep(5)
# window_handles() - Returns the handles of all windows within the current session
wh = driver.window_handles
print(wh)
print(len(wh))
# 3

# parent window
print(driver.title)

# child window1
driver.switch_to.window(wh[1])
print(driver.title)
time.sleep(3)
driver.find_element(By.ID, 't1').send_keys('akshara')
# driver.close()

# child window 2
driver.switch_to.window(wh[2])
print(driver.title)
driver.find_element(By.ID, 't2').send_keys('swara')
# driver.close()
time.sleep(4)