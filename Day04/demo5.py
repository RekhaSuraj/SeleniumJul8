import time

from selenium.webdriver import Chrome

driver = Chrome()

driver.get('http://www.google.com')

driver.set_window_size(400,300)
time.sleep(3)

x = 50
y = 50

for i in range(10):
    driver.set_window_size(x,y)
    x = x + 50
    y = y + 50
    time.sleep(2)


for i in range(10):
    driver.set_window_position(x,y)
    x = x+50
    y = y - 50
    time.sleep(2)
