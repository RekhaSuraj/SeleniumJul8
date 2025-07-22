# hw - https://swisnl.github.io/jQuery-contextMenu/demo.html
# alert popup - get text and click ok

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

driver = Chrome()
driver.get('file:///F:/Rekha/Rekha/BhanuClasses/Selenium/Pages/sample13.html')
time.sleep(2)
# For upload - we have to send the filepath in send_keys of the element
driver.find_element(By.ID,'A2').send_keys('F:/Rekha/Rekha/BhanuClasses/Selenium/Pages/sample12.html')

time.sleep(3)



