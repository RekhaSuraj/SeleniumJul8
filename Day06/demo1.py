from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("https://opensource-demo.orangehrmlive.com")
time.sleep(3)

driver.find_element(By.XPATH,"//input[@name='username']").send_keys('admin')
# driver.find_element(By.NAME, 'username')
time.sleep(3)
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("admin123")
time.sleep(3)

driver.find_element(By.XPATH,"//button[text()=' Login ']").click()

time.sleep(4)

# expected url
expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
current_url = driver.current_url
print(current_url)

if current_url == expected_url:
    print('Test case Pass')
else:
    print('Test case Fail')