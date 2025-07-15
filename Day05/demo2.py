# RelativeXPath : refers to locating elements on a webpage based on their relationships with other
# elements, starting from a specific context node.
# Unlike Absolute XPath, which provides the full path from the root of the HTML document,
# Relative XPath offers more flexibility and simplicity.

from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.by import By


driver = Chrome()
driver.get("file:///F:/Rekha/GRKTrainings/SeleniumJul8/Pages/sample4.html")
time.sleep(2)

driver.find_element(By.XPATH,"//input[1]").send_keys("abc")
driver.find_element(By.XPATH,"//input[2]").send_keys("xyz")

time.sleep(4)