from selenium import webdriver as wd
from bs4 import BeautifulSoup as bs

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait ### for waits
from selenium.webdriver.support import expected_conditions as EC ### for waits

import time
import sys
import pymysql as my

### load advanced data
base_url = "https://www.owasp.org/"

### load driver
driver = wd.Chrome(executable_path='/usr/local/bin/chromedriver')

### access site [GET]
driver.get(base_url)
### implicit waits
driver.implicitly_wait(10)
### accesss 'Attacks' category
driver.get(driver.find_element_by_id('n-Attacks').find_element_by_css_selector('a').get_attribute('href'))

### implicit waits
driver.implicitly_wait(10)

categories = driver.find_elements_by_class_name('mw-category-group')
print(len(categories))

### terminate program
driver.close()
driver.quit()
sys.exit()