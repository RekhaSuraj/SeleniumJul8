from selenium.webdriver import Chrome
import time

driver = Chrome()
driver.get("http://google.com")
time.sleep(2)

driver.get("http://www.facebook.com")
time.sleep(3)

# Browser goes back
driver.back()
time.sleep(2)

# Browser goes forward
driver.forward()
time.sleep(2)

# Refreshes the browser
driver.refresh()
time.sleep(2)

driver.close()