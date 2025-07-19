from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("https://www.globalsqa.com/")
time.sleep(5)
driver.maximize_window()
loc = driver.find_element(By.XPATH,"(//a[text()='Contact Us'])[1]").location
y = loc['y']
y = y + 400
print(y)
js = "window.scrollTo(0,"+str(y) + ")"
print(js)

driver.execute_script(js)
time.sleep(7)



