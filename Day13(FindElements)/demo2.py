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
time.sleep(15)
all_auto_suggestions[3].click()

# for ele in all_auto_suggestions:
#     if 'compiler' in ele.text:
#         ele.click()
#         break
#
time.sleep(4)








