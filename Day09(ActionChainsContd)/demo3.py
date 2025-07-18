# scrolling
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = Chrome()
driver.get('http://www.news.google.com')

time.sleep(2)

act = ActionChains(driver)
india_link = driver.find_element(By.XPATH,"(//a[text()='India'])[2]")
act.scroll_to_element(india_link)

time.sleep(2)
india_link.click()
time.sleep(6)


