import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

userName = khushburander_ca4jQ5
accessKey = os.environ['BROWSERSTACK_ACCESS_KEY']
localIdentifier = os.environ['BROWSERSTACK_LOCAL_IDENTIFIER']
buildName = os.environ['BROWSERSTACK_BUILD_NAME']
projectName = os.environ['BROWSERSTACK_PROJECT_NAME']

desired_cap = {
    'bstack:options' : {
        "os" : "Windows",
        "osVersion" : "10",
        "buildName" : "BStack Build Name: " + buildName,
        "projectName" : "BStack Project Name: " + projectName,
        "localIdentifier": localIdentifier,
        "seleniumVersion" : "4.0.0",
        "userName": username,
        "accessKey": accessKey
        },
    "browserName" : "Chrome",
    "browserVersion" : "100.0",
    }
options = ChromeOptions()
options.set_capability('bstack:options', bstack_options)
driver = webdriver.Remote(
    command_executor="https://hub.browserstack.com/wd/hub",
    options=options)
driver.get("http://localhost:8099") # HTTP Server should be running on 8099 port of GitHub runner
print(driver.title)
driver.quit()
