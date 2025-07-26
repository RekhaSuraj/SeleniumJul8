from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = Chrome()
driver.implicitly_wait(10)
driver.get('file:///F:/Rekha/GRKTrainings/SeleniumJul8/Pages/sample18.html')

driver.find_element(By.ID,"ok").click()

# Explicitly_wait - We have to give the condition of wait explicitly
# WebDriverWait () - Constructor, takes a WebDriver instance and timeout in seconds.
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.alert_is_present())

alrt = driver.switch_to.alert

print(alrt.text)
# OK button was clicked!
alrt.accept()
