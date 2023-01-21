import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as ChromeOptions

userName = 'khushburander_ca4jQ5'
accessKey = 'AnzFx7qCZUyqqSEe42ym'
localIdentifier = 'random'
buildName = 'test'
projectName = 'testing'

desired_cap = {
    'bstack:options' : {
        "os" : "Windows",
        "osVersion" : "10",
        "buildName" : "BStack Build Name: " + buildName,
        "projectName" : "BStack Project Name: " + projectName,
        "localIdentifier": localIdentifier,
        "seleniumVersion" : "4.0.0",
        "userName": "khushburander_ca4jQ5",
        "accessKey": "AnzFx7qCZUyqqSEe42ym"
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
