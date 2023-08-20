from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep


# create a new Chrome browser instance
service = Service(executable_path="/Users/jfernandez/QA/python-selenium-automation/chromedriver")
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url ... ('get' command = open, 'open browser')
driver.get('https://www.amazon.com/')

# input search text
driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('table')

# click search button
driver.find_element(By.ID, 'nav-search-submit-button').click()


expected_result = '"table"'
actual_result = driver.find_element(By.XPATH, '//span[@class="a-color-state a-text-bold"]').text
assert expected_result == actual_result, f'Expected {expected_result} did not match actual {actual_result}'

sleep(5)

print('Test case passed')

driver.quit()

