from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("file:///F:/Rekha/GRKTrainings/SeleniumJul8/Pages/sample2.html")

def go_back(driver):
    driver.back()
    time.sleep(3)


driver.find_element(By.CSS_SELECTOR,"a[id ='a1']").click()
go_back(driver)

# short cut code
driver.find_element(By.CSS_SELECTOR, "a#a1").click()
go_back(driver)

driver.find_element(By.CSS_SELECTOR, "#a1").click()
go_back(driver)

# class
# driver.find_element(By.CSS_SELECTOR, "a[class='c1']").click()

driver.find_element(By.CSS_SELECTOR, "a.c1").click()
go_back(driver)

driver.find_element(By.CSS_SELECTOR, ".c1").click()
go_back(driver)
