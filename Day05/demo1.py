from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.by import By

# Xpath - Path of an element in a html tree
# 1. Absolute Xpath
# 2. Relative Xpath

# Absolute XPath
# An absolute XPath is a way to locate elements in an HTML document by specifying the full path
# from the root of the document to the element

driver = Chrome()
driver.get("file:///F:/Rekha/GRKTrainings/SeleniumJul8/Pages/sample4.html")
time.sleep(2)

driver.find_element(By.XPATH,"//html//body//input[1]").send_keys("abc")
driver.find_element(By.XPATH,"//html//body//input[2]").send_keys("xyz")

time.sleep(4)


