from selenium.webdriver import Chrome
import time

driver = Chrome()
driver.get("https://opensource-demo.orangehrmlive.com")
time.sleep(2)

driver.maximize_window()
ele = driver.switch_to.active_element

# Enter data
ele.send_keys("admin")

time.sleep(4)