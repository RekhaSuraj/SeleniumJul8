from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("https://books-pwakit.appspot.com/")
time.sleep(2)

shadow_ele = driver.find_element(By.XPATH,"//html//body//book-app").shadow_root

# driver.find_element(By.ID,"input").send_keys('journal')
shadow_ele.find_element(By.ID,"input").send_keys('journal')
# driver.find_element(By.ID,"input").send_keys(Keys.ENTER)
shadow_ele.find_element(By.ID,'input').send_keys(Keys.ENTER)

time.sleep(5)
