from selenium.webdriver import Chrome
import time

driver = Chrome()
driver.get("http://www.google.com")

# driver.maximize_window()
cur_size = driver.get_window_size()

print(cur_size)
print(cur_size["width"])
print(cur_size['height'])

time.sleep(2)
# driver.set_window_size(700,450)
# time.sleep(3)

cur_pos = driver.get_window_position()
print(cur_pos)
print(cur_pos['x'])
print(cur_pos['y'])

driver.set_window_position(100,50)
time.sleep(3)






