from dotenv import load_dotenv
import os
import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from browserstack.local import Local
from selenium.common.exceptions import NoSuchElementException

#load_dotenv()
BROWSERSTACK_USERNAME = os.environ.get("BROWSERSTACK_USERNAME") or "BROWSERSTACK_USERNAME"
BROWSERSTACK_ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY") or "BROWSERSTACK_ACCESS_KEY"
URL = os.environ.get("URL") or "https://hub.browserstack.com/wd/hub"

# Creates an instance of Local
bs_local = Local()

# You can also set an environment variable - "BROWSERSTACK_ACCESS_KEY".
bs_local_args = { "key": BROWSERSTACK_ACCESS_KEY }

# Starts the Local instance with the required arguments
bs_local.start(**bs_local_args)

# Check if BrowserStack local instance is running
print("Local binary connected: ", bs_local.isRunning())

desired_cap = {
    "os" : "OS X",
    "osVersion" : "Sierra",
    "buildName" : "browserstack-build-1",
    "sessionName" : "BStack local python",
    "local" : "true",
    "userName": BROWSERSTACK_USERNAME,
    "accessKey": BROWSERSTACK_ACCESS_KEY
}
desired_cap["source"] = "python:sample-main:v1.0"
options = ChromeOptions()
options.set_capability('bstack:options', desired_cap)
driver = webdriver.Remote(
    command_executor=URL,
    options=options)
try:
	driver.get('https://www.amazon.in/')
	time.sleep(3)
	driver.maximize_window()
	SignIn_button = driver.find_element(By.XPATH,'//*[@id="nav-link-accountList"]/span')
	SignIn_button.click()
	username_textbox = driver.find_element(By.ID,"ap_email")
	username_textbox.send_keys(login_username)
	Continue_button = driver.find_element(By.ID,"continue")
	Continue_button.submit()
	password_textbox = driver.find_element(By.XPATH,"//input[@id='ap_password']")
	password_textbox.send_keys(login_password)
	SignIn_button = driver.find_element(By.ID,"auth-signin-button-announce")
	SignIn_button.submit()
	time.sleep(5)
	print("Login Successfull...")
finally:
    # Stop the driver
    driver.quit()
