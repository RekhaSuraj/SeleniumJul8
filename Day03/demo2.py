from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("file:///F:/Rekha/GRKTrainings/SeleniumJul8/Pages/sample2.html")
# driver.get("F:\\Rekha\\GRKTrainings\\SeleniumJul8\\Pages")

time.sleep(2)
# locators
# Id
# driver.find_element(By.ID,"a1").click()

# name
# driver.find_element(By.NAME,"n1").click()

# class
# driver.find_element(By.CLASS_NAME,"c1").click()

# Tag_name
# driver.find_element(By.TAG_NAME,"a").click()

# Link Text
# driver.find_element(By.LINK_TEXT,"Click Here").click()

# Partial link text
# driver.find_element(By.PARTIAL_LINK_TEXT,"Here").click()

driver.find_element(By.PARTIAL_LINK_TEXT,"Cli").click()
time.sleep(3)


