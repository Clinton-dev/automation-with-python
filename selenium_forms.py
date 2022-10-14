#! python 3.8.10
"""
selenium_forms.py fills in forms from  https://demo.seleniumeasy.com/basic-first-form-demo.html
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

driver.implicitly_wait(5)

# One input field
user_msg = driver.find_element('id', 'user-message')
show_msg = driver.find_element(
    'css selector', 'button[onclick="showInput();"]')

user_msg.send_keys('Hello world')
show_msg.click()

# explicitly wait
# WebDriverWait(driver, 15).until(
#     EC.text_to_be_present_in_element(
#         (By.CLASS_NAME, 'panel-heading'),
#         'Two Input Fields'
#     )
# )
driver.implicitly_wait(15)

# Two input fields
sum1 = driver.find_element('id', 'sum1')
sum2 = driver.find_element('id', 'sum2')

sum1.send_keys(Keys.NUMPAD8, Keys.NUMPAD2)
sum2.send_keys(4)

# click get total btn
driver.find_element('css selector', 'button[onclick="return total()"]').click()
