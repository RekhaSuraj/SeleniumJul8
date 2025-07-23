# close all child windows/browsers
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

driver = Chrome()
driver.get('file:///F:/Rekha/Rekha/BhanuClasses/Selenium/Pages/sample13.html')
time.sleep(2)

driver.find_element(By.ID,'A5').click()
time.sleep(3)

# current_window_handle - Returns the handle of the current window
parent = driver.current_window_handle

all_whls = driver.window_handles
print(all_whls)
# Remove parent from the window handles
all_whls.remove(parent)

for wh in all_whls:
    driver.switch_to.window(wh)
    # if we have to close a particular window
    if driver.title == 'swara':
        driver.close()
        time.sleep(2)

time.sleep(3)

