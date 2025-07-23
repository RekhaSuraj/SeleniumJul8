# close all open windows including parent window
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

driver = Chrome()
driver.get('file:///F:/Rekha/Rekha/BhanuClasses/Selenium/Pages/sample13.html')
time.sleep(2)

driver.find_element(By.ID,'A5').click()
time.sleep(3)
whls = driver.window_handles

# whls[0] - parent window
for wh in whls:
    driver.switch_to.window(wh)
    driver.close()
    time.sleep(2)

time.sleep(3)

