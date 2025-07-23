# To disable notifications

import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
driver = Chrome(options=chrome_options) # open chrome browser with the specified setting

# driver = Chrome()
driver.get('https://www.irctc.co.in/')
driver.maximize_window()
time.sleep(15)



