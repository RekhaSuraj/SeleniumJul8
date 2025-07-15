from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()

time.sleep(2)
driver.find_element(By.XPATH,"//input[@name='username']").send_keys('abc')

driver.find_element(By.XPATH,"//input[@type='password']").send_keys("xyz")

driver.find_element(By.XPATH,"//button[text()=' Login ']").click()

time.sleep(3)

err_msg = driver.find_element(By.XPATH,"//p[text()='Invalid credentials']")
print(err_msg.value_of_css_property("color"))
print(err_msg.value_of_css_property("font-family"))
print(err_msg.value_of_css_property("font-size"))
time.sleep(3)