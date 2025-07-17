from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("https://opensource-demo.orangehrmlive.com")

time.sleep(2)
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@name='username']").send_keys('abc')

driver.find_element(By.XPATH,"//input[@type='password']").send_keys("xyz")

driver.find_element(By.XPATH,"//button[text()=' Login ']").click()

time.sleep(3)

err_msg = driver.find_element(By.XPATH,"//p[text()='Invalid credentials']")

# get_screenshot_as_file('Filename')-Saves a screenshot of the current window to a PNG image file.
# Returns False if there is any IOError, else returns True. Use full paths in your filename.

# driver.get_screenshot_as_file("err_msg.png")

# screenshot('Filename') - Saves a screenshot of the current element to a PNG image file.
# Returns False if there is any IOError, else returns True. Use full paths in your filename
err_msg.screenshot('error_message.png')
time.sleep(2)