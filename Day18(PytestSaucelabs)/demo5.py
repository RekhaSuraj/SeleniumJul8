# Saucelabs.com - Third party grid

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

options = ChromeOptions()
options.browser_version = 'latest'
options.platform_name = 'Windows 11'
sauce_options = {}
sauce_options['username'] = 'oauth-rekhasuraj574-a4eb3'
sauce_options['accessKey'] = '5d67f115-3dbf-47ad-98a6-59f20600690b'
sauce_options['build'] = 'selenium-build-BDULZ'
sauce_options['name'] = 'PySelenium31July'
options.set_capability('sauce:options', sauce_options)

url = "https://ondemand.eu-central-1.saucelabs.com:443/wd/hub"
driver = webdriver.Remote(command_executor=url, options=options)

# Our test code starts here
# run commands and assertions
driver.get("http://www.google.com")
print(driver.title)
driver.quit()