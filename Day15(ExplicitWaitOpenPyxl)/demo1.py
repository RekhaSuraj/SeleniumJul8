from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = Chrome()
driver.get('file:///F:/Rekha/GRKTrainings/SeleniumJul8/Pages/sample14.html')
time.sleep(3)

chkboxs = driver.find_elements(By.XPATH,"//input[@type='checkbox']")

for ch in chkboxs:
    ch.click()

time.sleep(4)