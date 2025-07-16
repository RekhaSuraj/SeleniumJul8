from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("file:///F:/Rekha/GRKTrainings/SeleniumJul8/Pages/sample10.html")
time.sleep(2)

driver.find_element(By.ID,'A1').clear()
driver.find_element(By.ID,"A1").send_keys('admin')

# isdisplayed() - Whether the element is visible to a user
print(driver.find_element(By.ID,'A1').is_displayed())
# True
time.sleep(3)

print(driver.find_element(By.ID,'A3').is_displayed())
time.sleep(2)
# False

driver.find_element(By.ID,'A2').click()

driver.back()
time.sleep(5)

# is_enabled - Returns whether the element is enabled - Selenium can locate a hidden or disabled element as well
print(driver.find_element(By.ID,'A4').is_enabled())
# False

# is_selected - Returns whether the element is selected
print(driver.find_element(By.ID,'A5').is_selected())

print(driver.find_element(By.ID, 'A6').is_selected())

driver.find_element(By.ID,'A7').click()

driver.find_element(By.ID,'A8').click()

time.sleep(2)