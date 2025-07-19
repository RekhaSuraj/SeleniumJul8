# Iframes - switch_to.parent_frame() - only one level up
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
# Here we have given frame index as 0
driver.switch_to.frame(0) #go inside iframe
driver.find_element(By.ID,'t2').send_keys('xyz')

time.sleep(4)

# Switches focus to the parent context. If the current context is the top level browsing context,
# the context remains unchanged.
driver.switch_to.parent_frame()

driver.find_element(By.ID,'t1').clear()
driver.find_element(By.ID,'t1').send_keys('after frame')

time.sleep(4)

