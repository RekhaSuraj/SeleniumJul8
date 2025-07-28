# Create a class for a webpage and declaring all related elements and methods is called Page Object Model (POM)

# POM Class - Store elements and methods, it is also called repository class
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

class LoginPage:

    __un = (By.NAME,'username')
    __pwd = (By.NAME,'password')
    __login = (By.XPATH,"//button[@type='submit']")

    def __init__(self, driver):
        self.un_tb = driver.find_element(*self.__un)
        self.pwd_tb = driver.find_element(*self.__pwd)
        self.login_btn = driver.find_element(*self.__login)

    def set_username(self,un):
        self.un_tb.send_keys(un)

    def set_password(self,pwd):
        self.pwd_tb.send_keys(pwd)

    def click_login_btn(self):
        self.login_btn.click()


driver = Chrome()
driver.get('https://opensource-demo.orangehrmlive.com')
driver.implicitly_wait(10)

login_Page = LoginPage(driver)
login_Page.set_username('admin')
login_Page.set_password('admin123')
login_Page.click_login_btn()

time.sleep(5)


