from selenium.webdriver import Chrome
import time

driver = Chrome()
driver.get("http://www.google.com")
time.sleep(3)

# Maximizes the browser window
driver.maximize_window()
time.sleep(3)

driver.minimize_window()
time.sleep(2)

driver.maximize_window()
time.sleep(3)
# Closes the current browser
driver.close()