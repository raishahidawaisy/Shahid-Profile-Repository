from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://selenium.dev/')

time.sleep(1)

search_element = driver.find_element_by_xpath('//*[@id="gsc-i-id1"]')

#element.click()

#driver.back()


time.sleep(1)

search_element.click()

search_element.send_keys('webtesting')

from selenium.webdriver.common.keys import Keys
search_element.send_keys(Keys.RETURN)

time.sleep(1)

driver.switch_to.frame('master-1')
link_elements = driver.find_elements_by_tag_name('a')


print(link_elements[0].get_attribute('href'))



