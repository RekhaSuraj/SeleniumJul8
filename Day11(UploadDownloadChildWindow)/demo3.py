# Downloads
import os.path

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

driver = Chrome()
driver.get('file:///F:/Rekha/Rekha/BhanuClasses/Selenium/Pages/sample13.html')
time.sleep(2)

driver.find_element(By.ID,'A3').click()
time.sleep(4)

driver.find_element(By.XPATH,"//button[text()='Close']").click()

driver.find_element(By.ID,"PageLink_5").click()
time.sleep(2)
driver.find_element(By.ID,"DirectLink_6").click()
time.sleep(3)


# Verify if the file is downloaded
file_name = driver.find_element(By.ID,"DirectLink_6").text
# C:/users/suraj/Downloads/V3_BOQ_ItemRate_Template.xls
download_path = 'C:/users/suraj/Downloads/'+file_name

# Path verification
if os.path.exists(download_path):
    print('Download Successful')
else:
    print('File not downloaded')




