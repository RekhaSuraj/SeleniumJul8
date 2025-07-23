# Opening windows in tabs and windows

import time
from selenium.webdriver import Chrome

driver = Chrome()
driver.get('http://www.google.com')
time.sleep(3)

driver.switch_to.new_window('tab')
driver.get('http://www.fb.com')
time.sleep(3)

driver.switch_to.new_window('window')
driver.get('http://www.gmail.com')
time.sleep(3)

driver.switch_to.default_content()
