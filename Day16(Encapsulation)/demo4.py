import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

class LoginPage:

    __un = (By.NAME,'username')
    __pwd = (By.NAME,'password')
    __login = (By.XPATH,"//button[@type='submit']")

    def __init__(self, driver):
        self.driver = driver
        self.un_tb = driver.find_element(*self.__un)
        self.pwd_tb = driver.find_element(*self.__pwd)
        self.login_btn = driver.find_element(*self.__login)

    def set_username(self,un):
        self.un_tb.send_keys(un)

    def set_password(self,pwd):
        self.pwd_tb.send_keys(pwd)

    def click_login_btn(self):
        self.login_btn.click()


class HomePage:

    # __userPic = (By.CLASS_NAME,"oxd-userdropdown-name")
    # __logout = (By.XPATH,"//a[text()='Logout']")

    def __init__(self,driver):
        self.driver = driver
        self.__userPic_btn = (By.CLASS_NAME,"oxd-userdropdown-name")
        self.__logout_btn = (By.XPATH,"//a[text()='Logout']")

    def userPic_click(self):
        driver.find_element(*self.__userPic_btn).click()

    def click_logout(self):
        driver.find_element(*self.__logout_btn).click()


driver = Chrome()
driver.get('https://opensource-demo.orangehrmlive.com')
driver.implicitly_wait(10)

login_Page = LoginPage(driver)
login_Page.set_username('admin')
login_Page.set_password('admin123')
login_Page.click_login_btn()

time.sleep(2)

home_Page = HomePage(driver)
driver.implicitly_wait(10)
home_Page.userPic_click()
time.sleep(5)
home_Page.click_logout()
time.sleep(3)


