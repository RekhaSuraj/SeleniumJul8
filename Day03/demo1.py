from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.keys import Keys

driver = Chrome()
driver.get("https://opensource-demo.orangehrmlive.com")
time.sleep(3)
driver.maximize_window()

ele = driver.switch_to.active_element
ele.send_keys('admin')
time.sleep(3)

# Tab key would be called, and control goes to password textbox
ele.send_keys(Keys.TAB)

pwd = driver.switch_to.active_element
pwd.send_keys('admin123')

time.sleep(4)
# Tab key would be called and control goes to login button
pwd.send_keys(Keys.TAB)

btn = driver.switch_to.active_element

# Enter key would be called here and will be logged in into the application
btn.send_keys(Keys.ENTER)
time.sleep(4)