import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# The webdriver management will be handled by the browserstack-sdk
# so this will be overridden and tests will run browserstack -
# without any changes to the test files!
#driver = webdriver.Chrome()

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

userName = os.environ['BROWSERSTACK_USERNAME']
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


try:
    driver.get('https://bstackdemo.com/')
    WebDriverWait(driver, 10).until(EC.title_contains('StackDemo'))
    # Get text of an product - iPhone 12
    item_on_page = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="1"]/p'))).text
    # Click the 'Add to cart' button if it is visible
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="1"]/div[4]'))).click()
    # Check if the Cart pane is visible
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.CLASS_NAME, 'float-cart__content')))
    # Get text of product in cart
    item_in_cart = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div[2]/div/div[3]/p[1]'))).text
    # Verify whether the product (iPhone 12) is added to cart
    if item_on_page == item_in_cart:
        # Set the status of test as 'passed' if item is added to cart
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "iPhone 12 has been successfully added to the cart!"}}')
    else:
        # Set the status of test as 'failed' if item is not added to cart
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "iPhone 12 not added to the cart!"}}')
except NoSuchElementException as err:
    message = 'Exception: ' + str(err.__class__) + str(err.msg)
    driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": ' + json.dumps(message) + '}}')
except Exception as err:
    message = 'Exception: ' + str(err.__class__) + str(err.msg)
    driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": ' + json.dumps(message) + '}}')
finally:
    # Stop the driver
    driver.quit()
