import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time

login_username = "khushbu.rander@gmail.com"
login_password = "xxxxxxxxx"

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
