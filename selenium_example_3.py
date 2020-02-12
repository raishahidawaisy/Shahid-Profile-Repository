from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.get('http://automationpractice.com/index.php')

time.sleep(1)

#driver.find_element_by_xpath('//*[@id="block_top_menu"]/ul/li[3]/a').click()

product_containers = driver.find_elements_by_class_name('product-container')

time.sleep(2)

for index,product_container in enumerate(product_containers):
    hover = ActionChains(driver).move_to_element(product_container)
    hover.perform()
    #index+1 is for indexing in selenium list starts from 1, while in python list, it starts from zero
    driver.find_element_by_xpath('//*[@id="homefeatured"]/li[%s]/div/div[2]/div[2]/a[1]/span'%(index+1)).click()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="layer_cart"]/div[1]/div[2]/div[4]/span/span').click()
    time.sleep(1.5)
