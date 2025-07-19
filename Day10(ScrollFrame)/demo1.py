# scrolling
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

driver = Chrome()
driver.get('http://www.news.google.com')
driver.maximize_window()
time.sleep(2)

act = ActionChains(driver)

# scroll_by_amount(x,y) - Scrolls by provided amounts with the origin in the top left corner of the viewport.
# act.scroll_by_amount(0,500).perform()
#
# time.sleep(4)

act.scroll_by_amount(400,500).perform()

time.sleep(4)

india_link = driver.find_element(By.XPATH,"(//a[text()='India'])[2]")
act.scroll_to_element(india_link).perform()

time.sleep(5)
# print(help(ScrollOrigin))
scroll_origin = ScrollOrigin.from_element(india_link)

# scroll_from_origin(origin,x,y)- Scrolls by provided amount based on a provided origin.
# The scroll origin is either the center of an element or the upper left of the viewport plus any offsets.
# If the origin is an element, and the element is not in the viewport, the bottom of the element will first
# be scrolled to the bottom of the viewport

act.scroll_from_origin(scroll_origin,0,600).perform()
time.sleep(5)



