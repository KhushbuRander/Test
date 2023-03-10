from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os

userName = os.environ['BROWSERSTACK_USERNAME']
accessKey = os.environ['BROWSERSTACK_ACCESS_KEY']
localIdentifier = os.environ['BROWSERSTACK_LOCAL_IDENTIFIER']
buildName = os.environ['BROWSERSTACK_BUILD_NAME']
projectName = os.environ['BROWSERSTACK_PROJECT_NAME']

desired_cap = {
    'bstack:options' : {
        "os" : "Windows",
        "osVersion" : "10",
        "browserVersion" : "latest",
        "local" : "true",
        "seleniumVersion" : "3.14.0",
        },
    "browserName" : "Chrome",
    }

options = webdriver.ChromeOptions()
#MyHashMap<String, Object> bstackoptions = new MyHashMap<String, Object>();
options.set_capability('bstack:options', desired_cap)
driver = webdriver.Remote(
    command_executor="https://khushburander_ca4jQ5:AnzFx7qCZUyqqSEe42ym@hub.browserstack.com/wd/hub",
    options=options)
driver.get("http://localhost:8099") # HTTP Server should be running on 8099 port of GitHub runner
print(driver.title)
driver.quit()
