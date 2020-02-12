from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.google.com/')

element = driver.find_element_by_name('q')

element.send_keys('World politics')

from selenium.webdriver.common.keys import Keys

element.send_keys(Keys.RETURN)
