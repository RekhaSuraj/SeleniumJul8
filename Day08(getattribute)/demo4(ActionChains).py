# Action Chains - Mouse actions
from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("https://www.globalsqa.com")
time.sleep(3)
driver.maximize_window()

act = ActionChains(driver)
ele = driver.find_element(By.XPATH,"(//a[text()='Free Ebooks'])[1]")
# perform() has to be given for mouse actions
act.move_to_element(ele).perform()
time.sleep(3)

driver.find_element(By.XPATH,"//span[text()='Free Machine Learning Ebooks']").click()
time.sleep(3)



