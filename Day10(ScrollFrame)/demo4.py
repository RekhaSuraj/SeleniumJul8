# Iframes
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

driver = Chrome()
driver.get("file:///F:/Rekha/GRKTrainings/SeleniumJul8/Pages/sample12.html")
time.sleep(2)

driver.find_element(By.ID,'t1').send_keys('before frame entry')
time.sleep(4)

# switch_to - Returns: - SwitchTo: an object containing all options to switch focus into
# Switches focus to the specified frame, by index, name, or webelement.
# Here we have given frame id as f1
driver.switch_to.frame('f1') #go inside iframe
driver.find_element(By.ID,'t2').send_keys('xyz')

time.sleep(4)

# Switch focus to the default frame
driver.switch_to.default_content() #goto main html page

driver.find_element(By.ID,'t1').clear()
driver.find_element(By.ID,'t1').send_keys('after frame')

time.sleep(4)

