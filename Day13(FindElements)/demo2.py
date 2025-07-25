from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

driver = Chrome()
driver.get('http://google.com')
driver.maximize_window()
time.sleep(4)

driver.find_element(By.ID,"APjFqb").send_keys('python')
time.sleep(4)
# contains locator to be used
all_auto_suggestions = driver.find_elements(By.XPATH,"//span[contains(text(),'python')]")

# count
cnt = len(all_auto_suggestions)
print(cnt)
time.sleep(5)
all_auto_suggestions[4].click()

# for ele in all_auto_suggestions:
#     if 'compiler' in ele.text:
#         ele.click()
#         break
#
time.sleep(4)

# =======================================================================================
# Difference between find_element and find_elements:
# find_element                                    find_elements
# 1. Return Type is WebElement                   1. Return type is a list of Webelements
# 2. Returns first matching WE
# if any duplicates				                2. Returns address of all matching elements
# 3. If no matches,
# throws NSEE					                    3. Returns empty list










