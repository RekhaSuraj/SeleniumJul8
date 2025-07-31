# xdist - For parallel executions
# install package pytest-xdist
# In the terminal
# syntax: pytest -vs test_demo1.py -n 2 ij
# here -n 2 : 2 means 2 threads or worker processes, it can be any number

# For generating html report
# syntax: pytest -vs --html <report_name>.html
# For example: pytest test_demo1.py -vs --html report1.html
import time


import pytest
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox

def test_1():
    driver = Chrome()
    driver.get("http://www.google.com")
    print(driver.title)
    time.sleep(6)
    driver.quit()


def test_2():
    driver = Firefox()
    driver.get("http://www.fb.com")
    print(driver.title)
    time.sleep(6)
    driver.quit()


