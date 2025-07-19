# alert popups

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

driver = Chrome()
driver.get("file:///F:/Rekha/Rekha/BhanuClasses/Selenium/Pages/sample13.html")

driver.maximize_window()
time.sleep(2)

driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(2)
alert_popup = driver.switch_to.alert
# alert_popup.accept()
alert_popup.dismiss()
time.sleep(3)

