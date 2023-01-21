import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time

login_username = "khushbu.rander@gmail.com"
login_password = "xxxxxxxxx"

driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
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
