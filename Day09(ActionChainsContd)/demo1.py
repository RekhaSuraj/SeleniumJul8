from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# context_click - right click
driver = Chrome()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
time.sleep(2)
driver.maximize_window()

act = ActionChains(driver)
ele = driver.find_element(By.XPATH,"//span[text()='right click me']")
act.context_click(ele).perform()

time.sleep(2)
# driver.find_element(By.XPATH,"//span[text()='Copy']").click()
ele1 = driver.find_element(By.XPATH,"//span[text()='Copy']")
act.move_to_element(ele1).perform()
ele1.click()

time.sleep(2)

# hw - Cut, Paste,Delete - click
