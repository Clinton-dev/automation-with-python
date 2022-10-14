#! python3.8.10

""" Selenium basics opens https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html and clicks on  """
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# press f12 to find where its ref in file
driver = webdriver.Chrome()
driver.get(
    'https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html')

driver.implicitly_wait(30)
btn = driver.find_element('id', 'downloadButton')
btn.click()

# custom wait
WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'progress-label'),
        'Complete'
    )
)
