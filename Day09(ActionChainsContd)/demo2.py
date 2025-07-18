# doubleclick
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.color import Color
import time

driver = Chrome()
driver.get("https://www.plus2net.com/javascript_tutorial/ondblclick-demo.php")
time.sleep(2)
driver.maximize_window()

# text of the box before double clicking
box1 = driver.find_element(By.ID,"box")
msg_before = box1.text
print('Text in the box before double click:',msg_before)
# Text in the box before double click:Double Click here

# hw - print the background-color of the box before double clicking

btn = driver.find_element(By.XPATH,"//input[@value='Double Click']")
act = ActionChains(driver)
act.double_click(btn).perform()
time.sleep(2)

# color of the box
clr = box1.value_of_css_property('background-color')
print(clr)
# rgba(255, 204, 255, 1)

# hex format of the color - use hex
color_hex = Color.from_string(clr).hex
print(color_hex)
#ffccff

time.sleep(2)

# text of the box after double click
msg_after = box1.text
print('Text in the box after double click:',msg_after)
# Text in the box after double click:This is double click
