#! python3.8.10

""" Selenium basics opens https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html and clicks on  """
from selenium import webdriver

driver = webdriver.Chrome()
driver.get(
    'https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html')

driver.implicitly_wait(3)
btn = driver.find_element('id', 'downloadButton')
btn.click()
